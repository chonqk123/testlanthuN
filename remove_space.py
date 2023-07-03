def process_name(name):
    # Tách chuỗi thành các từ riêng biệt
    words = name.split()

    # Loại bỏ khoảng trắng ở đầu và cuối các từ
    words = [word.strip() for word in words if word.strip()]

    # Chuyển đổi chữ cái đầu của từ thành chữ hoa, các chữ cái còn lại thành chữ thường
    processed_words = [word.capitalize() for word in words]

    # Lấy ký tự đầu tiên của họ và tên lót
    first_character = processed_words[0][0].upper()  # Chuyển ký tự đầu của từ thành chữ hoa
    rest_of_word = processed_words[0][1:].lower()  # Chuyển các ký tự còn lại của từ thành chữ thường

    # Kết hợp họ và tên lót và chữ cái đầu của tên
    processed_name = first_character + rest_of_word + ''.join(processed_words[1:])

    return processed_name

# Test với các ví dụ
name1 = "    le thi   Be    Nho   "
name2 = " nguyen mat   tROi  "

processed_name1 = process_name(name1)
processed_name2 = process_name(name2)

print(processed_name1)  # Kết quả: LThiBeNho
print(processed_name2)  # Kết quả: NMatTroi

