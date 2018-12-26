import os
import shutil
from unittest.case import TestCase
from project_cli import initializer


class TestProjectCLI(TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            shutil.rmtree('./test_output')
        except FileNotFoundError:
            pass  # Better safe than sorry.
        initializer._DEFAULT_OUTPUT_DIR = './test_output'

    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree('./test_output')
        except FileNotFoundError:
            pass  # Better safe than sorry.

    def test_default_file_setup(self):
        args = _CMDArgs()
        args.yes = 'yes'
        initializer.setup(args)

        self.assertTrue(os.path.exists('./test_output'))
        self.assertTrue(os.path.exists('./test_output/project_cli'))
        self.assertTrue(os.path.exists('./test_output/project_cli/__init__.py'))
        self.assertTrue(os.path.exists('./test_output/project_cli/__main__.py'))
        self.assertTrue(os.path.exists('./test_output/tests'))
        self.assertTrue(os.path.exists('./test_output/tests/__init__.py'))
        self.assertTrue(os.path.exists('./test_output/tests/context.py'))
        self.assertTrue(os.path.exists('./test_output/tests/test_main.py'))
        self.assertTrue(os.path.exists('./test_output/README.rst'))
        self.assertTrue(os.path.exists('./test_output/setup.py'))


class _CMDArgs:
    pass
