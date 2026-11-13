class Student():
    def __init__(self, name , roll_number , marks1 , marks2 , marks3):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        print("Student Name: ", self.name)
        print("Roll Number: ",self.roll_number)

    def totalmarks(self):
        total = self.marks1 + self.marks2 + self.marks3
        print("Total Marks: ", total)

    def averagemarks(self):
        ave = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Average Marks: ", ave)

s1 = Student("Phani", 101, 85, 90, 95)
s2 = Student("Rahul", 102, 75, 80, 85)
s3 = Student("Kumar", 103, 90, 95, 88)

s1.display()
s1.totalmarks()
s1.averagemarks()

s2.display()
s2.totalmarks()
s2.averagemarks()

s3.display()
s3.totalmarks()
s3.averagemarks()