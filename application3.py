
cities=("izmir","ankara","istanbul","ağrı")
print(type(cities))
print(cities[0])
print(cities[3])
print(cities[:2])
print(cities[-2:])


new_tuple = ("izmir",[28,"mahmut"],(2,4,6),100)
print(new_tuple[1][1])
print(new_tuple[2][2])

new_tuple = ("istanbul")
print(type(new_tuple))
new_tuple = ("istanbul",) #virgül tuple olduğunu söylüyor.
print(type(new_tuple))

new_tuple = (4,8,[1,20]) #Tuple'ın içinde liste varsa değişebilir. direkt olsa değişmez
new_tuple[-1][0] = 50
print(new_tuple)

cities= ("istanbul","ankara","izmir")
print("izmir" in cities)
print("istan" in cities)


new_tuple = ("5","izmir",28,"ankara","5","izmir")
new_set = set(new_tuple)
print(new_set)
new_tuple = tuple(new_set)
print(new_tuple)

new_tuple2=tuple(set(new_tuple))
print(new_tuple2)

new_set = {"ahmet","mehmet","ayşe","fatma"}
new_set.add("faruk")
new_list = list(new_set)
print(new_list)


new_string = "jhgkfdhjkghkjdh"
new_set = {harf for harf in new_string }
print(new_set)

new_str= "ldfkljdsklklf"
new_set = {a for a in new_str}
print(new_set)
