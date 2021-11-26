class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def displayName(self):
        print(self.id, self.name)

if __name__=="__main__":
    student1=Student(1222, 'Lola')
    student1.displayName()
    student2 = Student(7777, 'Suga')
    student2.displayName()