class Student():
    student_count = 0

    def __init__(self , name , roll_number):
        self.name = name
        self.roll_number = roll_number
        Student.student_count += 1

    @classmethod
    def display_count(cls):
        print("Total Students:",cls.student_count)

s1 = Student("Phani", 101)
s2 = Student("Rahul", 102)
s3 = Student("Kumar", 103)

Student.display_count()

#print(Student.student_count)