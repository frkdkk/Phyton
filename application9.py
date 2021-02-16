
with open("data.txt","r") as my_file:

    print(my_file.read())
    my_file.seek(0)
    print(my_file.read(6))
    print(my_file.read(6))
    print(my_file.tell())


courses = ["Python", "Javascript", "C++", "Java", "Ruby"]
with open("courses.txt","w") as my_file:
    for course in courses:
        my_file.write(f"{course}\n")


with open("movies.txt", "r") as my_file:
    file_content = my_file.readlines()
    file_content = [element.strip("\n") for element in file_content if "\n" in element]
    print(file_content)


with open("movies.txt","r") as my_file:
    with open("movies2.txt","w") as my_file2:
        for line in my_file:
            my_file2.write(line)

with open("movies.txt","r") as text:
    with open("movies3.txt","w") as text3:
        for line in text:
            text3.write(line)
