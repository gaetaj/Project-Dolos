import hashlib
from uuid import uuid4
from src.utils import handle_directory


HASH_LENGTH = 32
OUTPUT_PATH = './output/'


def message_insert(binary_path):
    handle_directory(OUTPUT_PATH)
    binary = open(binary_path, 'rb')
    hashed_message = hashlib.sha256()
    message = str(uuid4())
    hashed_message.update(bytes(message, 'utf-8'))
    hashed_digested = hashed_message.digest()
    binary_contents = binary.read()
    binary_contents += hashed_digested
    new_binary = open(OUTPUT_PATH + binary_path, 'wb')
    new_binary.write(binary_contents)
    return hashed_digested.hex()


def message_retrieve(binary_path):
    binary = open(binary_path, 'rb')
    binary_contents = binary.read()
    return binary_contents[len(binary_contents) - HASH_LENGTH: len(binary_contents)].hex()
