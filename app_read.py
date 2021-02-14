#Dosya İşlemleri (Read)

my_file = open("movies.txt", "r")
file_content = my_file.read()
print(file_content)

print(my_file.name)
print(my_file.mode)

my_file.close()

print(my_file.closed)


with open("movies.txt", "r") as my_file:  #context manager yapısı 
    print(my_file.read())                 #(dosyaları kapatmaya gerek olmuyor)

print(my_file.closed)

with open("movies.txt", "r") as my_file:
    print(my_file.readline(), end="")
    print(my_file.readline())
    print(my_file.readlines())

with open("movies.txt", "r") as my_file:
    for line in my_file:
        print(line)

with open("movies.txt", "r") as my_file:
    print(my_file.read(12))
