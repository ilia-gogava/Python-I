"""ატვირთეთ სქრინები ან პირდაპირ ლინკები ამოხსნის აიასოფტის საიტიდან

https://www.aiasoft.ge/problem/333

https://www.aiasoft.ge/problem/332

https://www.aiasoft.ge/problem/331

https://www.aiasoft.ge/problem/330

https://www.aiasoft.ge/problem/329

https://www.aiasoft.ge/problem/328"""


#დავალება 1 #328 — ლუწი რიცხვები
a, b = int(input()), int(input())
shedegi = []
for i in range(a, b + 1):
    if i % 2 == 0:
        shedegi.append(str(i))
print(" ".join(shedegi))


#329 — კენტი რიცხვები 2
n = int(input())
shedegi = []
for i in range(n, 0, -1):
    if i % 2 != 0:
        shedegi.append(str(i))
print(" ".join(shedegi))


#330 — კენტი რიცხვები 3
a, b = int(input()), int(input())
if a > b:
    a, b = b, a
shedegi = []
for i in range(a, b + 1):
    if i % 2 != 0:
        shedegi.append(str(i))
print(" ".join(shedegi))
      
#331 — გამყპფები 
n = int(input())
shedegi = []
i = 1
while i * i <= n:
    if n % i == 0:
        shedegi.append(i)
        if i != n // i:
            shedegi.append(n // i)
    i += 1
shedegi.sort()
print(" ".join(map(str, shedegi)))

#332 — გამრავლების ტაბულა
n = int(input())
raodanoba = 0
i = 1
while i * i <= n:
    if n % i == 0:
        raodanoba += 1
        if i != n // i:
            raodanoba += 1
    i += 1
print(raodanoba)

#333 — კენტი გამყპფები
n = int(input())
jami = 0
i = 1
while i * i <= n:
    if n % i == 0:
        jami += i
        if i != n // i:
            jami += n // i
    i += 1
print(jami)