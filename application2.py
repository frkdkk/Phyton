dersler= ["matematik","fizik","kimya","ingilizce","türkçe"]
print(dersler[1].upper())
print(dersler[-1].upper())

print(dersler[0:2])
print(dersler[-2:])

dersler= ["matematik",["fizik","kimya"],"ingilizce","türkçe"] #nested list diye geçer
print(dersler[1])
print(dersler[1][0])
print(dersler[1][1])

print(dersler[len(dersler)-1])

dersler= ["matematik","fizik","kimya","ingilizce","türkçe"]
print(len(dersler))
dersler.append("Tarih")
dersler[len(dersler):]=["Coğrafya"]
print(dersler)


dersler.insert(0, "Biyoloji")
dersler.insert(len(dersler),"EMAT")
print(dersler)

del dersler[3]
dersler.remove("ingilizce")
print(dersler)


numbers=[1,6,9,5,8,4,3,6,5,7]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)


dersler= [["matematik","fizik"],["kimya","ingilizce"],["türkçe","tarih"]]
dersler2=[]
dersler2.append(dersler[0][1])
dersler2.append(dersler[1][1])
dersler2.append(dersler[2][1])
print(dersler2)


for ders in dersler:
    dersler2.append(ders[-1])

print(dersler2)


squares = []

for num in range(0,11):
    squares.append(num**2)

print(squares)

squares = [num**2 for num in range(0,11)]
print(squares)
