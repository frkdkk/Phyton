
num = 1
while num <=10:
    print(num)
    num+=1

mes=""
while mes!="quit":
    mes=input("quit yaz bitsin : ")
    print(mes)

while 5>3:
    print("5 3'ten her zaman büyüktür") #sonsuz döngü




my_flag = True
mess=""
while my_flag:
    mess=input("Çıkmak için quit yaz")
    if mess=="quit":
        my_flag = False
    else:
        print(mess)



num=1
while num<10:
    print(num)
    if num==5:
        break
    num+=1



num=1
while num<10:
    num+=1
    if num%2==0:
        continue
    print(num)
