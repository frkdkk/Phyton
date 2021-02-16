
print("Hello World")

#SyntaxError : Yazım hatası yapıldı anlamına geliyor.
#NameError : Tanımlanmamış isim.

#Yazdığın kodlaran mutlaka not ekle,daha iyi anlaşılabilmesi için.

#variable-value
n = 1
print(n)

p = n
print(p)

#DATA TYPES
#Integer
#Float-Ondalık sayı
#String-Karakter
#Boolean-Mantıksal değer
#Complex-Karmaşık sayılar
#Dictionary
#Tuple
#Set

hello = "World"
print(hello) #Hello : Değişken(Variable)
print("World")
print(n)

type(hello) #Hangi veri tipinde olduğunu çıktı veriyor.

#Integer
int_value = 5
print(type(int_value))

#Float
float_value = 3.19
print(type(float_value))
print(type("x"))

#Boolean
t, f =True, False
print(type(t))
print(t)
print(f)

#Swapping
data1 = 7
data2 = 12
data3 = 23.5
data4 = 33
data1,data2,data3,data4 = data2,data1,data4,data3
print(data1,data2,data3,data4)

print("data1 :",data1,"data2 :",data2)

#Lenght(Kaç değer veya kaç adet olduğunu bildirir.)
print(len("Pythoneer"))

data22="Data Science"
print(len(data22))

#f-string
name = "Turkey"
print(f"hello {name}")
print("Hello",name)

#Format
name2 = "Şelale"
print("Hello",format(name2))

#Sep : araya bir şeyler atıyor.
print("Hello","World",sep="\n") 

#Data Type Changing
data12=12
print(str(data12))
print(type(data12))

data12 = str(data12)
print(type(data12))

print(float("3"))
print(round(float("3.0")))

#Exponential numbers
def func():
    return 5**2
print(func())

print("35"*3)

x=10
print(x//2) #Virgülden sonrasını atıyor.
print(x%2) #Mod

z = 5
z+=2
z*=2

world = "Hello"
world2 = '%s %d' % (world, len(world))
print(world2)

hello = "Hello"
print(hello)
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4])

#IndexError : index hatası.

print(world)
print(world[-1])
print(world[-3])
print(world[-5])

job = "Engineering"
print(job[5])

print(hello[2:4])
print(hello[3:])
print(hello[:4])
print(hello[::-1]) #Kelimeyi tersten yazar.

print(world[2:4:2])

city = "İstanbul"
print("t" in city )

word = 'machine learning'
print(word.capitalize()) #Baş harfini büyütür
print(word.upper()) #Bütün harfleri küçültür
print(word.replace('machine','artificial')) #Değişim yapar

#strip() sağdan ve soldan silme yapıyor.
word2 = "          artificial general      intelligence"
print(word2.strip())
 
#Input aldığı değeri her zaman string'e çevirir.
y = input("Değer gir bakalım : ")
print(y)

#Lists
mylist = [3,5,6,7]
print(mylist)

a=5
b=5.0
print(a==b)



