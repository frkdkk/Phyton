

friends = ["ahmet","mehmet","ebru","mahmut","ayşe"]
x=0
while (x<len(friends)):
    friend=friends[x]
    x+=1
    if friend=="mahmut":
        continue
    print(friend)


for friend in friends:
    if friend=="mahmut":
        continue
    print(friend)


minNum=int(input("Minimum sayıyı giriniz : "))
maxNum=int(input("Maximum sayıyı giriniz : "))
for evenNum in range(minNum,maxNum):
        if evenNum%2!=0:
            continue
        else:
            print(evenNum)


import random
xnum=random.randint(1,100)
num =int(input("1-100 arasında sayı giriniz : "))
while num!=xnum:
    if num<xnum:
        print(f"{num}\'dan daha büyük bir sayı giriniz")
        num=int(input())
    else:
        print(f"{num}\'dan daha küçük bir sayı giriniz")
        num=int(input())

    print(f"Tebrikler {num}\'ı yakaladınız")



celcius=[20,25,30,35]
kelvin=[]
fahrenheit=[]
for c in celcius:
    k=c+273
    kelvin.append(k)
    f=c*9/5+32
    fahrenheit.append(f)
print(kelvin)
print(fahrenheit)



num=int(input("Lütfen bir sayı giriniz"))
if num<0:
    print("negatif sayı girdiniz")
else:
    sum=0
    while num > 0:
        sum+=num
        num-=1
    print("Toplam sayı",sum)
