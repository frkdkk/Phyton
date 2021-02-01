
def func():
    print("Hello World")


func()

def my_function(username="Faruk"):      #argüman
    print(f"Hello {username}")
my_function()
my_function("Mahmut")


def func(username,age=25):
    print(f"Merhaba {username},{age} yaşındasınız")
func("Arin",32)


def func1():
    return 5+10

def func2():
    print(6+10)  #dönen bir değer yok
result1=func1()
result2=func2()

print(f"Result 1,{result1}")
print(f"Result 2,{result2}")


def func():
    pass
func()

def func():
    print(5+7)
func()
print(func)  #fonksiyonun hafızadaki yeri


mylist=[1,4,7,3,9,4]
print(len(mylist))
myset=set(mylist)
print(myset)
print(type(myset))
print(sum(myset))


def func(x):
    return x**2
print(func(5))

y = lambda a: a**2
print(y(6))

besekle = lambda a: a+5
b=int(input("Sayı gir 5 eklesin: "))
print(besekle(b))

topla = lambda a,b: a+b
print(topla(10,7))

