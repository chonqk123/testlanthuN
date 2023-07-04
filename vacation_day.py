import datetime

# Hàm tính số ngày nghỉ phép
def calculate_leave_days(start_date):
    # Lấy ngày hiện hành từ hệ thống
    current_date = datetime.datetime.now().date()

    # Số ngày nghỉ đối với nhân viên làm trên 1 năm
    if start_date.year < current_date.year:
        years= current_date.year - start_date.year

        if years >= 5:
            return 14.0
        elif years >= 4:
            return 13.0
        else:
            return 12.0

    # Số ngày nghỉ đối với nhân viên mới vào làm năm nay
    elif start_date.year == current_date.year:
        days = (12 - start_date.month) + 1

        if start_date.day >= 10:
            return days - 0.5
        else:
            return days
    return 'ERORR'
def main():
    start_date_input = input("Nhập ngày vào làm (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_input, "%d/%m/%Y").date()
    leave_days = calculate_leave_days(start_date)
    print("Số ngày nghỉ phép: ", leave_days)

if __name__ == "__main__":
    main()

