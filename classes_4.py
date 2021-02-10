
# Inheritance (Kalıtım)

class Student:

    test = "Test Student" 

    def __init__(self, name, age, grades):
        self.name= name
        self.age= age
        self.grades= grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)


class UniversityStudent(Student):

    test= "Test University Student"

    def __init__(self, name, age, grades, university):
        super().__init__(name,age,grades)
        self.university= university

u_student_1=UniversityStudent("arin",21,[10,20,30],"SAÜ")

print(Student.test)
print(UniversityStudent.test)

#Student Class UniversityStudent Class'ının bir alt kümesi gibi,
#Class Student değişkenlerini UniversityStudent Class'ına çekebiliyoruz.
