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
    #tokenized_text = ViTokenizer.tokenize(quest).split()

    # Loại bỏ stop words
    #words = [word for word in tokenized_text if word.lower() not in stopwords]

    # Phân loại từ thành danh từ riêng, động từ, tính từ và danh từ
    tagged_word = ViPosTagger.pos_tag(quest)
    type_word = ["N", "Ny", "V", "A"]
    keys = [word[0] for word in tagged_word if word[1] in type_word]

    return keys
if __name__ == "__main__":
    print(load_stopwords())