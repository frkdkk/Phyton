# Çemberin alanını ve çevresini 2 ondalıklı olarak hesaplayınız.

pi=3.14159265
r=5

a=pi*r**2
c=2*pi*r

print("Alan :",round(a,2))
print("Çevre :",round(c,2))

#Math kütüphanesi kullanımı
import math
t=math.pi*r**2
print(round(t,2))


#Tek-Çift sayı
x=21
if(x%2==0):
    print("x bir çift sayı")
else:
    print("x bir tek sayıdır")

##
a="Python Code"
print(a)
print(type(a))

##
c="Faruk"
print("Benim adım "+c)
print("Benim adım {} ".format(c))
print(f"Benim adım {c}")

##
name="Faruk"
surname="Adak"
age=21
print(name,surname,age)

##
a=50
b="100"
print(int(b)+a)
print(str(a)+b)

#İnput
mystring=input("İsim nedir? ?\n")
print(mystring.upper())
print(mystring.lower())
