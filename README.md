# automatic-question-answering
-----Vi-----
# Hệ thống tự động trả lời câu hỏi theo thông tin trong tài liệu


# Tài liệu
## giải thích cây thư mực
    app/ - Thư mực chưa các module chính. mõi file .py được xem là một module chứ các hàm để sử lý một công việc nhất định.
    test/ - thư mực này chưa các module để test các module chính trong thư mực app/
    data/ - thư mục chưa dữ liệu file input, output... 
    requirements.txt - file chứa tên các thư viện cần cài đặt
    main.py file thư thi chính của dữ án (hiện đang trống)
## các module
    app/keyword.py module trích xuất keys từ 1 câu
        khai báo:
            from app import keyword
        hàm:
            keyword.list_keys(text)
                tham số "text" là câu đưa vào
                trả về 1 danh sách keys
                vi du: 
                    tham số : test = "cho em hỏi quy chế tin chỉ là gì?"
                    trả về: ["quy_chế", "tín chỉ"]
    app/docx.py module tách đoạn file word
        khai báo:
            from app import docx
        hàm:
            docx.list_paragraphs(file_path)
                tham số: file_path là đường dẫn file word
                trả về: danh sách các đoạn văn bản
    app/tool.py mou