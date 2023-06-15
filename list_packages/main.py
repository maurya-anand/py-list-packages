import pkg_resources

def list_installed_packages():
    """
    Retrieve a list of installed Python packages.

    Returns:
        list: List of dictionaries containing package information.
            Each dictionary contains the following keys:
                - 'Package': Package name
                - 'version': Package version
                - 'pip_string': Pip install string for the package
    """
    installed_packages = []
    for d in pkg_resources.working_set:
        [pkg_name, ver] = str(d).split(" ")
        pip_str = str(d).replace(" ", "==")
        installed_packages.append({'Package': pkg_name, 'version': ver, 'pip_string': pip_str})
    return installed_packages

def main(output='print'):
    """
    Entry point for listing installed packages.

    Args:
        output (str, optional): Output format.
            'print': Print the list of installed packages (default)
            'list': Return the list of installed packages

    Returns:
        None or list: Depending on the output format, either None or the list of installed packages.
    """
    installed_packages = list_installed_packages()

    if output == 'print':
        print("Package\tversion\tpip_string")
        for i in sorted(installed_packages, key=lambda x: x['Package']):
            print(f"{i['Package']}\t{i['version']}\t{i['pip_string']}")
    elif output == 'list':
        return installed_packages
    else:
        raise ValueError(f"Invalid output format: {output}")

if __name__ == '__main__':
    main()
