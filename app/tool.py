import os

def cre_file_path(path):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), path)

def get_files_directory(directory, type_file = ""):
    docx_files = []
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.{type_file}') or type_file == "":
                docx_files.append(os.path.join(foldername, filename))
    return docx_files
