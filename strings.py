 
name = "Farad Engineering"

print(len(name))
print(name[2])
print(name[3:6])  #3 dahil 6 dahil değil.
print(name[:6])
print(name.title()) #baş harfleri büyütür.
print(name.upper())

named="SAYDIM"
print(named.lower())

print(name.count("k")) #seçilen harfi saydırır.
print(name.find("k")) #seçilen harfin sırası.

print(name.replace("Engineering","Muhendislik"))

print(dir(name)) #Kullanılabilecek fonksiyonlar.

print(help(str)) #Kullanılabilecek metodlar. 

print(help(str.lower)) #Ne işe yaradığını gösterir.
