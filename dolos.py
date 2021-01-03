import argparse
from os import path
from src.linux.find_padding import find_padding

def main():
    parser = argparse.ArgumentParser(description='Steganography Tool to Identify Binary/Project Leakers')
    parser.add_argument('binary_path', help='Path to leaked binary')
    args = parser.parse_args()
    assert_valid_arguments(args)
    find_padding(args.binary_path)
    return 0


def assert_valid_arguments(args):
    assert path.exists(args.binary_path), 'Path provided does not exist'


if __name__ == '__main__':
    main()
