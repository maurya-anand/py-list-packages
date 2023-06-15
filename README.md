# list_packages

![example workflow](https://github.com/maurya-anand/py-list-packages/actions/workflows/python-package.yml/badge.svg)

`list_packages` is a Python package that allows you to list the installed Python packages along with their versions and pip install strings.

## Installation

To install `list_packages`, follow these steps:

1. Clone or download the repository from GitHub to your local computer.

2. Open a terminal or command prompt and navigate to the root directory of the downloaded repository.

3. (Optional) It is recommended to create a virtual environment to isolate the package dependencies. Run the following command to create a virtual environment (assuming you have `venv` installed):

```bash
   cd list_packages
   python3 -m venv env
   pip3 install -e .
```

## Usage

### Terminal

After installing the package, you can run the list-packages command in the terminal to list all installed Python packages:

``` bash
   list_packages
```

### Python Script/Notebook

To use list-packages in a Python notebook, you can import the list_packages module and call the list_installed_packages() function:

``` python
   from list_packages import list_installed_packages
   list_installed_packages()
```
