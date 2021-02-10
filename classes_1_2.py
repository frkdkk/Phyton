
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def brandmodel(self):
        return f"Araba markası {self.brand} ve modeli {self.model}"

car_1 = Car("BMW","i5",2010)
car_2 = Car("Audi","x6",2012)

print(car_1)
print(car_1.brand)
print(car_1.brandmodel())




class Movie:
    def __init__(self,name,director):
        self.name = name
        self.director = director

movie_1 = Movie("Full Metal Jacket","Kubrick")
movie_2 = Movie("Babel","Irarutu")

print(movie_1.name)
print(movie_2.director)
        


class Student:

    school_name = "X Lisesi"    #Class Variable
    number_of_students = 0

    def __init__(self,name,age,grades):
        self.name=name              #Instance Variable
        self.age=age
        self.grades=grades
        Student.number_of_students +=1

    def average(self):
        return sum(self.grades)/len(self.grades)

    def schoolName(self):
        return f"Okulumuzun adı {self.school_name}"

student_1 = Student("Faruk",21,[80,60,50])
student_2 = Student("Mevlüt",20,[80,40,70])


print(Student.school_name)
print(student_1.schoolName())

print(Student.__dict__)
print(student_1.__dict__)


print(Student.number_of_students)

print(student_1.average())
print(student_2.average())


#Class değişkenleri daha geneli kapsar. Instance değişkenler ise 
# verilen özelliklere göre daha spesifiktir. İkisi de class'ta
# tanımlanırlar.
# Class variable sadece bir nesneyi tutar, Instance variable ise
# birden fazla nesneyi tutar.
