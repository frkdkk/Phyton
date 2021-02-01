

def kare(x):
    return x**2

x= int(input("Karesini istediğiniz sayıyı giriniz : "))
print(f"Girilen {x} sayısının karesi {kare(x)}")


x=int(input("Lütfen sayı giriniz: "))
y=int(input("Lütfen bir sayı daha griniz: "))
top = lambda x,y:x+y 
çarp = lambda x,y : x*y
print(f"Girilen sayıların toplamı : {top(x,y)} , çarpımı : {çarp(x,y)}")

def multiply(mylist):
    mult = 1
    for x in mylist:
        mult *=x 
    return mult
list1=[3,5,6,10]
print(multiply(list1))


def fakt(a):
    if a==0:
        return 1
    else:
        return a*fakt(a-1)
a=int(input("Sayı gir : "))
print(fakt(a))


def cube_c(a):
    return 12*a
def cube_(a):
    return 6*a**2
def cube_v(a):
    return a**3

a=int(input("Kenar uzunluğu gir : "))
print(f"Kenarı {a} olan küpün çevresi : {cube_c(a)}, alanı : {cube_a(a)}, hacmi : {cube_v(a)}")
