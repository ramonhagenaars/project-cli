import os
import re
from project_cli.templates import (get_main, get_init, get_readme, get_setup,
                                   get_context, get_main_test_suite)


if os.name == 'nt':
    ENV_USER = 'USERNAME'
else:
    ENV_USER = 'USER'


_DEFAULT_NAME = os.getcwd().split(os.sep)[-1]
_DEFAULT_DESCRIPTION = 'A Python %s' % _DEFAULT_NAME
_DEFAULT_VERSION = '0.1.0'
_DEFAULT_AUTHOR = os.getenv(ENV_USER)
_DEFAULT_RUNNABLE = 'yes'
_DEFAULT_CORRECT = 'yes'
_DEFAULT_OUTPUT_DIR = './'

try:
    input_ = raw_input  # Python2.7
except NameError:
    input_ = input  # Python3.+


def setup(cmd_args):
    defaults = (_DEFAULT_NAME, _DEFAULT_OUTPUT_DIR, _DEFAULT_DESCRIPTION,
                _DEFAULT_VERSION, _DEFAULT_AUTHOR, _DEFAULT_RUNNABLE)
    inputs = defaults if cmd_args.yes else _get_user_inputs()
    _do_setup(*inputs)


def _do_setup(name, output_dir, description, version, author, runnable):
    main_package = os.path.join(output_dir, name)
    tests_package = os.path.join(output_dir, 'tests')

    os.makedirs(main_package, exist_ok=True)
    os.makedirs(tests_package, exist_ok=True)

    _create_file('README.rst', get_readme(name, description, runnable),
                 output_dir)
    _create_file('setup.py', get_setup(name, version, author, description,
                                       runnable), output_dir)
    _create_file('__init__.py', get_init(), main_package)
    _create_file('__main__.py', get_main(name), main_package)
    _create_file('__init__.py', get_init(), tests_package)
    _create_file('context.py', get_context(), tests_package)
    _create_file('test_main.py', get_main_test_suite(name, runnable),
                 tests_package)


def _is_yes(user_input):
    return user_input.lower() in ('yes', 'y')


def _get_input(message, default, regex=None, requirements=None):
    user_input = input_('%s (%s) ' % (message, default)) or default
    if regex:
        match = re.match(regex, user_input)
        if not match or match.group(0) != user_input:
            print('Invalid input. %s' % requirements)
            print('')
            return _get_input(message, default, regex, requirements)
    return user_input


def _get_user_inputs():
    name = _get_input('Project name', _DEFAULT_NAME, '[a-zA-Z_]\w*',
                      'A project name must be a word; it must start with a ' +\
                      'letter or underscore and may contain only letters, ' +\
                      'underscores and numbers in the remainder.')
    output_dir = _get_input('Output directory', './')  # TODO: validate it!
    description = _get_input('Description', 'A Python %s' % name)
    version = _get_input('Initial version', _DEFAULT_VERSION,
                         '[0-9]\.[0-9]\.[0-9]',
                         'A version must have the form: x.y.z where x, y ' +\
                         'and z are all whole numbers.')
    author = _get_input('Author', _DEFAULT_AUTHOR)
    runnable = _is_yes(_get_input('Is the project runnable?',
                                  _DEFAULT_RUNNABLE))

    print('')
    print('Setup overview')
    print('--------------')
    print('Project name:    %s' % name)
    print('Output dir:      %s' % os.path.abspath(output_dir))
    print('Description:     %s' % description)
    print('Initial version: %s' % version)
    print('Author:          %s' % author)
    print('Runnable:        %s' % ('yes' if runnable else 'no'))
    print('')
    correct = _is_yes(_get_input('Is this correct?', _DEFAULT_RUNNABLE))
    if not correct:
        print()
        return _get_user_inputs()
    return name, output_dir, description, version, author, runnable


def _create_file(fname, content, pname=None):
    output_path = os.path.abspath(os.path.join(pname, fname))
    with open(output_path, 'w+') as f:
        f.write(content)
