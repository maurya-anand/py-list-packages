import pkg_resources
import json

def list_installed_packages():
    """
    Retrieve a list of installed Python packages.

    Returns:
        list: List of dictionaries containing package information.
            Each dictionary contains the following keys:
                - 'Package': Package name
                - 'version': Package version
                - 'depends': A dictionary of dependencies.
                eg: {'Jinja2': '3.1.2', 'depends': {'markupsafe': '>=2.0'}}
    """
    installed_packages = []
    for d in pkg_resources.working_set:
        [pkg_name, ver] = str(d).split(" ")
        dependencies = []
        for dep in d.requires():
            dep_name = None
            dep_ver = None
            if dep.key:
                dep_name = dep.key
            if str(dep.specifier):
                dep_ver = str(dep.specifier)
            dependencies.append({'package': dep_name, 'version' :dep_ver})
        if dependencies:
            installed_packages.append({'package': pkg_name, 'version': ver, 'depends': dependencies})
        else :
            installed_packages.append({'package': pkg_name, 'version': ver, 'depends': None})
    return installed_packages

def main(output='list'):
    """
    Entry point for listing installed packages.

    Args:
        output (str, optional): Output format.
            'print': Prints a tabular output of installed packages and their dependencies (default). Columns: Package and Dependenc(y|ies)(comma seperated items).
                        Example: requests==2.31.0    charset-normalizer<4,>=2,certifi>=2017.4.17,idna<4,>=2.5,urllib3<3,>=1.21.1
            'list': Returns a JSON formatted list of installed packages and their dependencies.
                        Example: [
                                    {"package":"idna","version":"3.4","depends":null},
                                    {"package":"Jinja2","version":"3.1.2","depends":[{"package":"markupsafe","version":">=2.0"}]}
                                ]

    Returns:
        None or list: Depending on the output format, either None or the list of installed packages.
    """
    installed_packages = list_installed_packages()

    if output == 'print':
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
            print (f"{package['package']}=={package['version']}\t{dep_string}")
    elif output == 'list':
        json_string = json.dumps(installed_packages)
        print(json_string)
        return installed_packages
    else:
        raise ValueError(f"Invalid output format: {output}")

if __name__ == '__main__':
    main()
