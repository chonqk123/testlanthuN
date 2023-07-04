class Student:
    def __init__(self, name, math, literature, english):
        self.name = name
        self.math = math
        self.literature = literature
        self.english = english

    # khởi tạo phương thức tính điểm trung bình
    def avg(self):
        return (self.literature + self.math + self.english) / 3

class Manager:
    def __init__(self):
        self.students = []

    # Add từng student vào list
    def add_student(self, student):
        self.students.append(student)

    # Lấy giá trị điểm trung bình lớn nhất của mảng
    def max_avg(self):
        highest_avg = 0
        for student in self.students:
            avg_score = student.avg()
            if avg_score > highest_avg:
                highest_avg = avg_score
        return highest_avg

    # In ra thông tin tên, điểm các môn, điểm trung bình của các học sinh đã nhập.
    def print_all_information(self):
        for student in self.students:
            print(f"name: {student.name}, toan: {student.math}, van: {student.literature}, anh: {student.english}, avg: {student.avg()}")

    # Sinh viên có điểm trung bình cao nhất
    def print_highest_average_students(self):
        highest_avg = self.max_avg()
        highest_avg_students = [student for student in self.students if student.avg() == highest_avg]
        print("Danh sách các học sinh có điểm trung bình cao nhất:")
        for student in highest_avg_students:
            print(f"name: {student.name}, toan: {student.math}, van: {student.literature}, anh: {student.english}, avg: {student.avg()}")

        
def main():
    student_manager = Manager()

    # Nhập thông tin sinh viên bao gồm số học sinh và điểm của các môn
    n = int(input("Số học sinh: "))
    for i in range(n):
        name = input("Tên học sinh: ")
        math = float(input("Điểm toán: ") )
        literature = float(input("Điểm văn: ") )
        english = float(input("Điểm anh: "))

        student = Student(name, math, literature, english)
        student_manager.add_student(student)

    highest_average = student_manager.max_avg()
    print("Điểm trung bình cao nhất của lớp là:", highest_average)

    student_manager.print_all_information()
    student_manager.print_highest_average_students()

if __name__ == "__main__":
    main()

