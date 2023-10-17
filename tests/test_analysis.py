import sys, os
# Thêm đường dẫn đến thư mục chứa my_module vào sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from app.analysis import get_keys

text = "cho em hỏi quy chế tín chỉ là gì?"
print(app.get_keys(text))
