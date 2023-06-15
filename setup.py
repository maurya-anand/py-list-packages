from setuptools import setup, find_packages

setup(
    name='list_packages',
    version='1.0.0',
    description='A package to list installed Python packages',
    author='Anand Maurya',
    author_email='anandmaurya@hotmail.com',
    platforms=['Any'],
    packages=find_packages(),
    url='https://github.com/maurya-anand/py-list-packages',
        entry_points={
        'console_scripts': ['list_packages=list_packages.main:main']
    },
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
)
