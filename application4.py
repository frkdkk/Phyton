
#boş liste
list1 = []
list2 = list()
print(type(list1))
print(type(list2))

#boş tuple
tuple1 = ()
tuple2 = tuple()
print(type(tuple1))
print(type(tuple2))

#boş set
set2= set()
print(type(set2))

#boş dict
dict1 = {}
dict2= dict()
print(type(dict1))
print(type(dict2))


friends = {"musa":21,"akif":23,"hakan":21}
print(friends["akif"])
print(sum(friends.values())/len(friends))


friends = {"fatih" : 99,"kütük" : 218}
friends["eren"] = 76
print(friends)
del friends["kütük"]
print(friends)
friends.update({"fatih": 91,"eren":666})
print(friends)


my_dict = {"odd_numbers": [1,2,3]}
my_dict = {my_dict["odd_numbers"][0]** 2, my_dict["odd_numbers"][1]** 2, my_dict["odd_numbers"][2]** 2}
print(my_dict)

my_dict2 = {"even numbers" : [2,4,6,8,10]}
for a in my_dict2.values():
    my_list = []
    for b in a:
        my_list.append(b**2)

my_dict2["even_numbers"] = my_list
print(my_dict2)


my_friends = {"ali" : 26,"mahmut" : 25,"ayşe" : 24}
my_key_list = []
my_value_list = []

for k,v in my_friends.items():
    my_key_list.append(k)
    my_value_list.append(v)

print(my_key_list)
print(my_value_list)
print(sum(my_value_list))
    
numbers = {x : x**2 for x in range(1,11)}
print(numbers)
