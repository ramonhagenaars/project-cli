import argparse
from project_cli import project_setup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--yes', action='store_true',
                        help="Say 'yes' to all prompts")
    args = parser.parse_known_args()[0]
    project_setup.setup(args)


if __name__ == '__main__':
    main()
