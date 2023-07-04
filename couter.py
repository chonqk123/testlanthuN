from collections import Counter

# Nhập số nguyên N là số lượng phần tử list
N = int(input("Nhập số lượng phần tử: "))

# Nhập danh sách N phần tử
elements = input("Nhập các phần tử: ").split()

# Sử dụng Counter để đếm số lần xuất hiện của từng phần tử
counter = Counter(elements)

# Sắp xếp kết quả theo thứ tự tăng dần theo số lần xuất hiện
sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1]))


print(sorted_counter)
