import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))


from app import keyword

def test1():
    QUESTION = [
        "mã môn học của môn quy hoạch tuyến tính?",
        "cho em hỏi quy chế tín chỉ là gì?",
        "Làm sao để đăng ký môn học?"
    ]

    for ques in QUESTION:
        print(keyword.list_keys(ques))

if __name__ == "__main__":
    test1()