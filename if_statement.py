
age = 15
if age>=18:
    print("Oy kullanabilirsiniz")
else:
    print("Oy Kullanamazsınız.")



my_list = ["ahmet","mehmet","ebru"]
if "ahmet" in my_list:
    print("Ahmet listede.")



if age<=2:
    print("%80 indirimli")
elif age<=10:
    print("%50 indirimli")
else:
    print("İndirimsiz")


age=int(input("Yaşınızı giriniz "))
if age<0:
    print("Negatif sayı giremezsiniz")
elif age==0:
    print("Lütfen sıfırdan farklı bir sayı giriniz")
elif age<18:
    print("Oy Kullanamazsınız")
else:
    print("Oy kullanabilirsiniz")


my_condition={}
if my_condition:
    print("Koşul doğru")
else:
    print("Koşul yanlış")
