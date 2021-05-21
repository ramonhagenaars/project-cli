BR = '\n'


def get_init():
    return ''


def get_main(name):
    return '"""This module serves as the entry point of ' + name + '."""' + BR \
           + BR \
           + BR \
           + 'def main():' + BR \
           + '    """The actual entry point."""' + BR \
           + '    raise NotImplementedError()' + BR \
           + BR \
           + BR \
           + "if __name__ == '__main__':" + BR \
           + '    main()' + BR


def get_readme(name, description, runnable):
    result = name + BR \
             + len(name) * '=' + BR \
             + BR \
             + description + BR
    if runnable:
        result += BR \
                  + 'Usage' + BR \
                  + "'''''" + BR \
                  + BR \
                  + '::' + BR \
                  + BR \
                  + '    python -m ' + name + BR

    result += BR\
              + "Testing" + BR\
              + "'''''''" + BR\
              + BR\
              + "::" + BR\
              + BR\
              + "    python -m unittest discover tests" + BR
    return result


def get_setup(name, version, author, description, runnable):
    result = '"""This is the installation toolset for this project."""' + BR \
             + "from setuptools import setup, find_packages" + BR \
             + BR \
             + "with open('README.rst', 'r') as fh:" + BR \
             + "    long_description = fh.read()" + BR \
             + BR \
             + "setup(name='" + name + "'," + BR \
             + "      version='" + version + "'," + BR \
             + "      author='" + author + "'," + BR \
             + "      description='" + description + "'," + BR \
             + "      long_description=long_description," + BR \
             + "      packages=find_packages(exclude=('tests',))"
    if runnable:
        result += "," + BR \
                  + "      entry_points={" + BR \
                  + "          'console_scripts': [" + BR \
                  + "              '" + name + " = " + name + ".__main__:main'" \
                  + BR \
                  + "          ]" + BR \
                  + "      }"
    result += ")" + BR
    return result


def get_context():
    return '"""Import this module first before importing your project stuff '\
           'in the tests"""' + BR\
           + "import sys" + BR\
           + "import os" + BR\
           + BR\
           + "dname = os.path.dirname(__file__)" + BR\
           + "relpath = os.path.join(dname, '..')" + BR\
           + "abspath = os.path.abspath(relpath)" + BR\
           + "sys.path.insert(0, abspath)" + BR


def get_main_test_suite(name, runnable):
    result = '"""Contains a test suite for basic tests."""' + BR\
             + "import tests.context" + BR\
             + "import unittest" + BR
    if runnable:
        result += "from " + name + ".__main__ import main" + BR
    result += BR\
              + BR\
              + "class MainTestSuite(unittest.TestCase):" + BR\
              + '    """Basic test cases."""' + BR
    if runnable:
        result += BR\
                  + "    def test_main(self):" + BR\
                  + "        with self.assertRaises(NotImplementedError):" + BR\
                  + "            main()" + BR
    result += BR\
              + BR\
              + "if __name__ == '__main__':" + BR\
              + "    unittest.main()" + BR
    return result
