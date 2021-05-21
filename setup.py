"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='project_cli',
      version='0.2.2',
      author='Ramon Hagenaars',
      description='A commandline interface for creating project structures',
      long_description=long_description,
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'project_cli = project_cli.__main__:main'
          ]
      })
