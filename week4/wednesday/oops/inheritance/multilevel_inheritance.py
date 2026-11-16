class Grandfather:
    def __init__(self , grandfather_name):
        self.grandfather_name = grandfather_name

    def display_grandfather(self):
        print("Grandfather Name:" , self.grandfather_name)

class Father(Grandfather):
    def __init__(self, grandfather_name , father_name):
        super().__init__(grandfather_name)
        self.father_name = father_name

    def display_father(self):
        print("Father Name:" , self.father_name)

class Son(Father):
    def __init__(self, grandfather_name, father_name , son):
        super().__init__(grandfather_name, father_name)
        self.son = son

    def display_son(self):
        print("Son Name:", self.son)

son = Son("Narayana", "Eswar", "Phani")

son.display_grandfather()
son.display_father()
son.display_son()