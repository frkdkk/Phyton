
#key-value çifti 
#(indisler sayı değil kelime veya harftir) sırasızdır
#dizi = ["key": "value"]

monster_1 = ["guru",10,"red"]
monster_1 = {"name" : "guru","power" : 10,"color" : "red"} 
my_friend = {"name" : "deniz","age" : 21,"gender" : "female"}

print(type(my_friend))
print(my_friend)
print(my_friend["name"])

my_friend["position"] = "single"
print(my_friend)

print(my_friend.get("height")) 
#get kullanılınca listede olmayan şey none olarak çıkıyor.

my_friend.update({"name": "DENİZ","position": "taken"})
print(my_friend)
#update ekstra parametre ekleyebilir

del monster_1["power"]  #temelli silinir
poplan = monster_1.pop("color")  #silinir daha sonra kullanılabilir
print(monster_1)
print(poplan)

monster_1.clear() #içindekileri siler
print(monster_1)

print(len(my_friend))

print(my_friend.keys()) #key değerleri
print(my_friend.values()) #value değerleri
print(my_friend.items()) #key ve value birlikte gösterir

for key in my_friend:
    print(key)

for values in my_friend.values():
    print(values)


my_friends =[ 
    {"name":"mıza","age":21},
    {"name":"melih abim","age":21},
    {"name":"haker","age":21},
    {"name":"kerim abim","age":21}
]

for a in range(0,4): 
    for value in my_friends[a].values():
      print(value)
    



 


































































