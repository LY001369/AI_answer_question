import os

def crefilepath(path):
    return os.path.join(os.path.dirname(__file__), '..', path)