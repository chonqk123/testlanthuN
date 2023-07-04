def process_name(full_name):
    # Tách họ và tên thành danh sách các từ
    words = full_name.split()
    
    # Lấy tên và chuyển đổi chữ thường, viết hoa chữ cái đầu
    first_name = words[-1].capitalize()

    # Ngoại trừ cụm từ cuối trong list (tên)
    # Lấy chữ cái đầu của tất cả các cụm còn lại
    # Viết hoa lên và add vào short_last_name
    short_last_name = ''.join([word[0].upper() for word in words[:-1]])

    # Ghép họ và tên
    name = first_name + short_last_name

    return name


full_name = input("Nhập họ và tên: ")
name = process_name(full_name)
print("Họ và tên đã xử lý:", name)
