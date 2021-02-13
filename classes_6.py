
#Property Dekoretörü : Fonksiyonun değişken gibi kullanılması.

class Student:

    def __init__(self,name , surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
       

    def average(self):
        return sum(self.grades) / len(self.grades)

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"



student_1= Student("arin", "yazilim", 21, [10,20,30])

student_1.name="Mahmut"
student_1.grades = [50,50,50]

print(student_1.name)
print(student_1.surname)
print(student_1.fullname)
print(student_1.average())
