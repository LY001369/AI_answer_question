from docx import Document

def extract_text_from_docx(docx_path):
    # Mở file word
    doc = Document(docx_path)

    full_text = ""
    for paragraph in doc.paragraphs:
        full_text += paragraph.text + "\n"
    return full_text

def split_text_into_paragraphs(text):
    # Tách văn bản thành các đoạn văn dựa trên dấu xuống dòng trống
    paragraphs = text.split('\n\n')
    return paragraphs

def list_paragraphs(docx_path):

    # Trích xuất văn bản từ tệp Word
    word_text = extract_text_from_docx(docx_path)

    # Tách thành các đoạn văn
    paragraphs = split_text_into_paragraphs(word_text)

    return paragraphs

if __name__ == "__main__":
    pass
