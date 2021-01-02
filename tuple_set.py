

# Tuple (Demet) Elemanlar değiştirilemez.

capitals = ("tahran","ankara","madrid","tiflis")
print(len(capitals))
print(capitals[0])
print(capitals[1:3])
 # capitals[0]="izmir"

for yaz in capitals:
    print(yaz)

print(capitals)
capitals = ("berlin","roma")
print(capitals)
del capitals
print(capitals)



#Set (Küme) Elemanlar tek olma durumundadır.Sıra yoktur.Sırayı rastgele atar.

cities= {"izmir","ankara","istanbul","kars","istanbul"}
print(type(cities))
print(cities)
# print(cities[0]) yazdırmaz
cities.add("gaziantep")
print(cities)
cities.update(["edirne","trabzon"])
print(cities)
cities.remove("ankara")
print(cities)
# cities.remove("muğla")  hata alırsın

cities.discard("muğla") #hata almazsın
print(cities)  

cities.clear()  #içini temizler
print(cities)

del cities  #her şeyi siler
