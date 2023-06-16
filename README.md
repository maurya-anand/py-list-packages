# list_packages

![example workflow](https://github.com/maurya-anand/py-list-packages/actions/workflows/python-package.yml/badge.svg)

A utility to retrieve a list of installed Python packages and their dependencies.

Link to the [documentation](https://py-list-packages.readthedocs.io/).

## Installation

Install via Terminal:

1. Clone or download the repository from GitHub to your local computer.

2. Open a terminal or command prompt and navigate to the root directory of the downloaded repository.

3. (Optional) It is recommended to create a virtual environment to isolate the package dependencies. Run the following command to create a virtual environment (assuming you have `venv` installed):

```bash
cd list_packages
python3 -m venv env
pip3 install -e .
```

Install via Pip:

``` python
pip install git+https://github.com/maurya-anand/py-list-packages.git
```

## Usage

### Terminal

After installing the package, you can run the list-packages command in the terminal to list all installed Python packages and their dependencies:

``` bash
list_packages
```

### Python Script/Notebook

To use list-packages in a Python notebook, you can import the list_packages module and call the list_installed_packages() function:

``` python
## import
from list_packages import list_installed_packages
```

## Examples

### Terminal

``` bash
list_packages
```

Output

``` bash
Package                 Dependency
setuptools==59.6.0      None
Jinja2==3.1.2           markupsafe>=2.0
requests==2.31.0        charset-normalizer<4,>=2,certifi>=2017.4.17,urllib3<3,>=1.21.1,idna<4,>=2.5
```

### Python script/Notebook

By default, the function returns a list of dictionaries containing package information. Each dictionary has the following keys:

- package: Package name (str)
- version: Package version (str)
- depends: List of dictionaries containing package information (list)

``` python
from list_packages import list_installed_packages

installed_packages = list_installed_packages()
```

Output

``` python
[{'setuptools': '59.6.0', 'depends': None},{'package': 'Jinja2', 'version': '3.1.2', 'depends': [{'package': 'markupsafe', 'version': '>=2.0'}]}]
```

If you want the output in JSON format, you can pass the format='json' parameter to the list_installed_packages() function. It will return a JSON-formatted string representing the list of installed packages.

``` python
from list_packages import list_installed_packages

installed_packages = list_installed_packages('json')
```

Output

``` json
[
  {
    "package": "setuptools",
    "version": "59.6.0",
    "depends": null
  },
  {
    "package": "Jinja2",
    "version": "3.1.2",
    "depends": [
      {
        "package": "markupsafe",
        "version": ">=2.0"
      }
    ]
  }
]
```
