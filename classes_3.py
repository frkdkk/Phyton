
#Instance Method - Class Method - Static Method

class Student:

    school_name = "X Lisesi"
    number_of_students = 0

    def __init__(self,name,age,grades):
        self.name=name                        #Instance Method
        self.age=age
        self.grades=grades
        Student.number_of_students +=1

    def average(self):
        return sum(self.grades)/len(self.grades)

    @classmethod
    def display_school_name(cls ,name_of_school):
        cls.school_name= name_of_school             #Class Method

    @staticmethod
    def static():                                   #Static Method
        return f"Sadece bu mesaj yazıyor"



student_1 = Student("Faruk",21,[80,60,50])
student_2 = Student("Mevlüt",20,[80,40,70])

print(Student.static())
print(student_1.static())
print(student_2.static())
