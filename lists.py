
cities=["İzmir","Antalya","Ankara","İstanbul","Sakarya"]
print(cities[3])
print(cities[-1]) ##Sondan başlar
print(cities[:2])
print(cities[:-1])
cities[1]="Eskişehir"
print(cities)
cities.append("Ordu") ##Sona ekler
print(cities)
cities.insert(0,"Kars")
print(cities)
del cities[0] ##Silinen şeye ulaşılamaz
print(cities) 

cities=["İzmir","Antalya","Ankara","İstanbul","Sakarya"]
print(cities)
cities.pop()
print(cities)
cities2=cities.pop()
print(cities2)

cities=["İzmir","Antalya","Ankara","İstanbul","Sakarya"]
cities.remove("Ankara")
print(cities)

cities=["izmir","antalya","ankara","istanbul","sakarya"]
print(cities)
cities.sort()  ##Alfabetik sıralama
print(cities)
cities.sort(reverse=True) ##Alfabe tersten sıralama
print(cities) 




cities=["izmir","antalya","ankara","istanbul","sakarya"]
print(cities)
print(sorted(cities))
print(cities)



numbers=[11,22,33,56]
print(min(numbers))
print(max(numbers))
print(sum(numbers)) ##Toplamları



cities=["tokyo","madrid","londra","kiev"]
print(cities.index("londra")) ##Sırasını verir
print("ankara" in cities)  ##Listede oup olmadığını kontrol
print("tokyo" in cities)

for a in cities:
    print(a)



cities=["tokyo","madrid","kiev","londra"]
for a in cities:
    print(f"Gezilemeyen yer : {a}")



str_cities= "tokyo,madrid,kiev"
print(str_cities)
my_list=str_cities.split(", ") ## tırnak içindeki şeye göre ayırır
print(my_list)

str_email = "faruk0799@gmail.com"
my_list2=str_email.split("@")
print(my_list2)




for a in range(1,10):
    print(a)

for b in range(2,21,2):
    print(b)

numbers=list(range(1,11))
print(numbers)

numbers= [number for number in range(1,11)]
print(numbers)

cities=["ankara","izmir","afyon"]
print(cities)
cities2=cities[:]
print(cities2)
cities.append("artvin")
print(cities)
print(cities2)













































































































