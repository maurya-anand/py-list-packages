import unittest
from list_packages.main import list_installed_packages

class TestListPackages(unittest.TestCase):
    def test_list_installed_packages(self):
        
        packages = list_installed_packages()
        self.assertIsNotNone(packages)
        self.assertIsInstance(packages, list)
        self.assertTrue(len(packages) > 0)

if __name__ == '__main__':
    unittest.main()
