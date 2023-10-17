import sys, os
# Thêm đường dẫn đến thư mục chứa my_module vào sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from app import analysis

text = "cho em hỏi quy chế tín chỉ là gì"
a = analysis.load_stopwords()
print(a)