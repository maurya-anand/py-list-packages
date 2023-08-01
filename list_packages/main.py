import pkg_resources
import json
import sys


def list_installed_packages(format='list'):
    """
    Retrieve a list of installed Python packages.

    :param format: Output format. Defaults to 'list'. Accepts 'list' or 'json'.
    :type format: str

    :return: List of dictionaries containing package information. If format='json', a JSON string is returned.
    :rtype: list or str

    Each dictionary contains the following keys:
        - 'package' (str): Package name.
        - 'version' (str): Package version.
        - 'depends' (list): List of dictionaries containing package information.

    Example:
        [{'package': 'Jinja2', 'version': '3.1.2', 'depends': [{'package': 'markupsafe', 'version': '>=2.0'}]}]

    If format='json', the function returns a JSON-formatted string representing the list of installed packages.
    """
    installed_packages = []
    for pkg_obj in pkg_resources.working_set:
        [pkg_name, ver] = str(pkg_obj).split(" ")
        dependencies = []
        for dep in pkg_obj.requires():
            dep_name = None
            dep_ver = None
            if dep.key:
                dep_name = dep.key
            if str(dep.specifier):
                dep_ver = str(dep.specifier)
            dependencies.append({'package': dep_name, 'version': dep_ver})
        if dependencies:
            installed_packages.append({'package': pkg_name, 'version': ver, 'depends': dependencies})
        else:
            installed_packages.append({'package': pkg_name, 'version': ver, 'depends': None})
    if format == 'json':
        return json.dumps(installed_packages)
    else:
        return (installed_packages)


def command_line():
    """
    :meta private:
    """
    installed_packages = list_installed_packages()
    if len(sys.argv) > 1 and sys.argv[1] == 'json':
        json_string = json.dumps(installed_packages, indent=2)
        print(json_string)
    else:
        print("Package\tDependency")
        for package in installed_packages:
            dep_list = []
            dep_string = None
            if package['depends']:
                for dep in package['depends']:
                    if dep['version']:
                        dep_list.append(dep['package']+dep['version'])
                    else:
                        dep_list.append(dep['package']+'')
            if dep_list:
                dep_string = ','.join(dep_list)
            print(f"{package['package']}=={package['version']}\t{dep_string}")


if __name__ == '__main__':
    command_line()
