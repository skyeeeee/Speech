import os

def cleanfile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)