def overtime(check_in, check_out):
    # Chuyển đổi thời gian check-in và check-out thành số giờ
    check_in_hour, check_in_minute = map(int, check_in.split(":"))
    check_out_hour, check_out_minute = map(int, check_out.split(":"))
    total_check_in_minutes = check_in_hour * 60 + check_in_minute
    total_check_out_minutes = check_out_hour * 60 + check_out_minute

    # Kiểm tra tính hợp lệ của thời gian check-in và check-out
    if total_check_out_minutes < total_check_in_minutes:
        return "Thời gian không hợp lệ!"

    # Tính số giờ OT
    overtime_hours = (total_check_out_minutes - total_check_in_minutes) / 60

    # Kiểm tra các điều kiện và trả về kết quả tương ứng
    if overtime_hours > 4 and total_check_in_minutes <= 12* 60 and total_check_out_minutes >= 13 * 60:
        overtime_hours -= 1
        lunch = "Y"
        dinner = "N"
    elif overtime_hours > 3 and total_check_out_minutes>= 21 * 60:
        lunch = "N"
        dinner = "Y"
    else:
        lunch = "N"
        dinner = "N"

    return f"OT: {overtime_hours}, Lunch: {lunch}, Dinner: {dinner}"

def main():
    check_in = input("Thời gian Check-in (hh:mm): ")
    check_out = input("Thời gian Check-out (hh:mm): ")
    result = overtime(check_in, check_out)
    print(result)

if __name__ == "__main__":
    main()
