class Student():

    def __init__(self):     
        self.__marks = 80

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self , new_marks):
        if(new_marks < 0 or new_marks > 100):
            print("Reject")
        else:
            print("Marks updated successfully")
            self.__marks = new_marks
    

a = Student()
print("Initial Marks:", a.marks)
a.marks = 200
print("Current Mark:",a.marks)
a.marks = 100
print("Final Marks:",a.marks)