class Academic:

    def __init__(self , student_name):
        self.student_name = student_name

    def study(self):
        print("Student is studying")

class Sports:

    def play_sports(self):
        print("Student is playing sports")

class Student(Academic , Sports):

    def __init__(self, student_name , roll_number):
        super().__init__(student_name)
        self.roll_number = roll_number

    def display_details(self):
        print("Student Name:" , self.student_name)
        print("Student Roll_number:", self.roll_number)

student = Student("Phani", 101)

student.study()
student.play_sports()
student.display_details()