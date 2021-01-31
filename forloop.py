

numbers= [3,7,5,9,11]
for x in numbers:
    print(x)

friends={"ahmet","ebru","deniz","mahmut"}
for friend in friends:
    print(friend)

my_string = "electronics"
for letters in my_string:
    print(letters)


for x in range(1,11):
    print(x)

for x in range(1,11,2):
    print(x)


friends={"mahmut":36,"ayşe":32,"ahmet":41,"ebru":28}
for key,value in friends.items():
    if key=="ahmet":
        continue

    print(key,value)


friends = ["ahmet","mehmet","ali","hakan","can"]
for i,friend in enumerate(friends):
    print(i,friend)
