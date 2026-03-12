"""1) გაქვთ სია სტრინგებით, დაბეჭდეთ მხოლოდ ის სიტყვები რომელთა სიგრძე 5-ზე მეტია.

2)გაქვთ სია რიცხვებით, შექმენით ახალი სია სადაც იქნება მხოლოდ ლუწი რიცხვები, ასევე ამოშალეთ დუპლიკატები

3)გაქვთ ორი სია, იპოვეთ საერთო ელემენტები და მათი ჯამური რაოდენობა.

4)გაქვთ ლექსიკონი ქულებით, დაალაგეთ სტუდენტები ქულების კლებადობით და დაბეჭდეთ top 3.

5)გაქვთ სია სიტყვებით, დააჯგუფე ისინი პირველი ასოს მიხედვით dictionary-ში.

დაწერეთ თქვენი სიტყვებით, რა განსხვავებაა თითოეულ მონაცემთა სტრუქტურას შორის, რაც ვისწავლეთ, დეტალურად. ჩამოწერეთ თითოეულის ფუნქციები და ახსენით რას აკეთებენ ისენი."""

#დავალება 1
sitqvebi = ["გამარჯობა", "კატა", "პროგრამირება", "სახლი", "პითონი", "კი"]

for sitqva in sitqvebi:
    if len(sitqva) > 5:
        print(sitqva)

#დავალება 2
ricxvebi = [1, 2, 3, 4, 4, 6, 6, 8, 10, 10]

luwi = []

for i in ricxvebi:
    if i % 2 == 0 and i not in luwi:
        luwi.append(i)

print(luwi)

#დავალება 3
sia1 = [1, 2, 3, 4, 5]
sia2 = [3, 4, 5, 6, 7]

saerto = []

for i in sia1:
    if i in sia2:
        saerto.append(i)

print("საერთო ელემენტები:", saerto)
print("რაოდენობა:", len(saerto))

#დავალება 4
students = {
    "გიორგი": 85,
    "ანა": 92,
    "დავითი": 78,
    "მარიამი": 95,
    "ლუკა": 88
}

dasortirebi = sorted(students, key=lambda x: students[x], reverse=True)

print("TOP 3:")
for i in range(3):
    print(i+1, "-", dasortirebi[i], ":", students[dasortirebi[i]])

#დავალება 5
sitqvebi = ["ანა", "ბანანი", "ავტობუსი", "გიორგი", "გამარჯობა", "ბავშვი"]

jgufebi = {}

for sitqva in sitqvebi:
    asoi = sitqva[0]
    if asoi not in jgufebi:
        jgufebi[asoi] = []
    jgufebi[asoi].append(sitqva)

print(jgufebi)