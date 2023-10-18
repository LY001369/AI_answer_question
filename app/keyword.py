from .tool import crefilepath
from pyvi import ViPosTagger, ViTokenizer
import json, os

# Hàm tải lên stopword 
def load_stopwords():
    # Đường dẫn đến tệp JSON chứa danh sách stop words
    file_path = crefilepath('data/rss/stopword_vi.json')

    # Mở tệp JSON và nạp dữ liệu
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = json.load(file)["words"]
    
    return stopwords

def list_keys(quest):
    stopwords = load_stopwords()

    # Phân tách từ
    tokenized_text = ViTokenizer.tokenize(quest)

    # Phân loại từ 
    tagged_word = ViPosTagger.postagging(tokenized_text)

    # chon cac loai tu co the lam key
    type_word = ["N", "Nc", "Ny", "Np", "Nu", "M", "V", "A"]
    words = [word for word, type in zip(tagged_word[0], tagged_word[1]) if type in type_word]

    # Loại bỏ stop words
    keys = [word for word in words if word.lower() not in stopwords]

    return keys

if __name__ == "__main__":
    text = "Cho em hỏi quy chế tín chỉ là gì?"
    print(list_keys(text))