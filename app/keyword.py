from pyvi import ViPosTagger, ViTokenizer
import json, os

# Hàm tải lên stopword 
def load_stopwords():
    # Đường dẫn đến tệp JSON chứa danh sách stop words
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'rss/stopword_vi.json')

    # Mở tệp JSON và nạp dữ liệu
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = json.load(file)["words"]
    
    return stopwords

def get_keys(quest):
    stopwords = load_stopwords()

    # Phân tách từ
    tokenized_text = ViTokenizer.tokenize(quest)

    # Phân loại từ 
    tagged_word = ViPosTagger.postagging(tokenized_text)

    # chon cac loai tu co the lam key
    type_word = ["N", "Ny", "V", "A"]
    keys = [word[0] for word in tagged_word if word[1] in type_word]

    # Loại bỏ stop words
    keys = [word for word in tagged_word if word.lower() not in stopwords]

    return keys

if __name__ == "__main__":
    print(load_stopwords())