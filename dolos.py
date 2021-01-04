import argparse
from os import path
from src.message_handler import message_insert, message_retrieve

def main():
    parser = argparse.ArgumentParser(description='Steganography Tool to Identify Binary/Project Leakers')
    parser.add_argument('binary_path', help='Path to leaked binary')
    parser.add_argument('--retrieve', action='store_true', help='Retrieves value from binary')
    parser.add_argument('--insert', action='store_true', help='Insert a value into binary')
    args = parser.parse_args()
    assert_valid_arguments(args)
    if(args.insert):
        hash_returned = message_insert(args.binary_path)
        print('HASH INSERTED ', hash_returned)
    elif(args.retrieve):
        hash_returned = message_retrieve(args.binary_path)
        print('HASH FOUND ', hash_returned)
    return 0


def assert_valid_arguments(args):
    assert path.exists(args.binary_path), 'Path provided does not exist.'
    assert args.retrieve or args.insert, 'Not enough arguments provided.'
    assert not (args.retrieve and args.insert), 'Retrieve and Insert are mutually exclusive.'


if __name__ == '__main__':
    main()
