#Dosya işlemleri (Write)

with open("data.txt", "w") as my_file:
    my_file.write("star wars 1 \n")
    my_file.seek(0)          #başlangıçtan itibaren üzerine yazıyor
    my_file.write("Mahmut\n")
    print("The Godfather 1", file = my_file)



#Dosya işlemleri (Append)

with open("data.txt","a") as my_file:
    my_file.write("Superman")

#Dosya işlemleri (Create)

with open("data3.txt", "x") as my_file:
    my_file.write("Python\n")
    my_file.write("Django")
