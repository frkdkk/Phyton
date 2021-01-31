

num1 = int(input("Lütfen bir sayı giriniz : "))
if num1 %2 == 0:
    print(f"{num1} Girdiğiniz sayı çifttir. ")
else:
    print(f"{num1}Girdiğiniz sayı tektir. ")


num2 = int(input("Bir sayı giriniz : "))
if num2<0:
    print(f"{num2} sayısı sıfırdan küçüktür")
elif num2>0:
    print(f"{num2} sayısı sıfırdan büyüktür")
elif num2==0:
    print(f"{num2} sayısı sıfıra eşittir")



x = 10
y = 5
if x>5: print(f"{x} sayısı {y}'ten büyüktür. ")


x = 10
y = 15
print(f"{x} sayısı {y}\'den büyüktür") if x > y else print(f"{x} sayısı {y}\'den küçüktür")


number = int(input("Bir sayı giriniz"))
fakt=1
if number<0:
    print(f"{number} sayısı negatiftir")
elif number==0:
    print(f"{number} sayısının faktöriyeli {fakt}")
else:
    for x in range(1,number+1):
        fakt=fakt*x
    print(f"{number} sayısının faktöriyeli {fakt}")




notes = {"ahmet":58,"mehmet":76,"ebru":44,"pınar":90}
for key,value in notes.items():
    if value>=50:
        print(f"{key} aldığı not {value} : GEÇTİ")
    else:
        print(f"{key} aldığı not {value} : KALDI")
