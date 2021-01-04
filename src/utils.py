import os

def handle_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)
