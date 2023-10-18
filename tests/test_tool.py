import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))
#===============================================================================

from app import tool

print(tool.get_files_directory(tool.cre_file_path("data/docx")))