
#Dictionaries

#Key-Value yani Anahtar-Değer çiftini depolamak için kullanılır.
#Sıralıdır.
#Değiştirilebilir.
#Kopyalanamaz.
#Value değeri, bütün data tiplerinde olabilir.



#Dictionaries direkt bu parantezler ile oluşturulabilir.
myDict = {}        
print(type(myDict))



#Key değeri girilerek value değeri çıktısı alınabilir.
dict = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964,
}
print(dict)
print(dict["model"])  



#Aynı key ismi yine aynı key isminin üzerine yazılır.
dict = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964,
"year" : 2010         
}
print(dict["year"])



#Len fonksiyonu ile kaç Key-Value çiftinin 
#kaldığını bize gösterir.
dict = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964,
"year" : 2010  
}
print(len(dict))  


#"get" fonksiyonu ile  key var olmayan key değeri için none döner.
#Var olan key değeri için ise value değeri döner.
print(dict.get("brand")) 
print(dict.get("age"))



#"update" fonksiyonu ile ekstra Key-Value çifti eklenebilir.
dict.update({"color": "black","price": "10k€"})
print(dict)



#"del" fonksiyonu ile Key-Value çifti tamamen silinir.
del dict["year"]
print(dict)  


#"pop" fonksiyonu ile Key-Value çifti silinir 
# ama daha sonra kullanılabilir.
dict.pop("color")
print(dict)


#"clear" fonksiyonu ile dictionaries'in içindekiler silinir.
dict.clear()
print(dict)



#Value,Keys,Items parametrelerini yazdırır.
dict = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964,
}
print(dict.values())
print(dict.keys())
print(dict.items())



#for döngüsü ile Key ve Value parametrelerini yazdırmak.
for key in dict.keys():
    print(key)
for value in dict.values():
    print(value)
for item in dict.items():
    print(item)


#for döngüsü ile dizi içindeki dictionaries parametrelerinin 
#value'lerini yazdırmak.
myDict = [
{"name" : "Faruk","age" : 21},
{"name" : "Fatih","age" : 9},
{"name" : "Furkan","age" : 16}
]

for a in range(0,3):
    for value in myDict[a].values():
        print(value)

