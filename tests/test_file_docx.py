import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))
#======================================================================#

from app import docx, tool
def test1():
    file_path = tool.cre_file_path("data/doc/Lectures.docx")
    print(file_path)
    paragraphs = docx.list_paragraphs(file_path)
    for para in paragraphs:
        print('-' * 50)
        print(para)
    
if __name__ == "__main__":
    test1()