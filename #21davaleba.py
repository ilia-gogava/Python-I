"""პროგრამამ უნდა სთხოვოს მომხმარებელს 3 ადამიანის სახელი და ჩაწეროს ფაილში names.txt ისე, რომ ყოველი სახელი იყოს ახალ ხაზზე.

წაიკითხე ფაილი (მაგალითად animals.txt) და დაბეჭდე:

რამდენი ხაზი აქვს ფაილს

რა წერია პირველ ხაზზე

შექმენი პროგრამა, რომელიც გამოიყენებს append რეჟიმს. ყოველ გაშვებაზე მომხმარებელს უნდა ჰკითხოს შეტყობინება და დაამატოს იგი ფაილ log.txt-ში.

მოცემული სია:

 
products = ["Bread\n", "Milk\n", "Apple\n", "Juice\n"]
ჩაწერე ეს მონაცემები ფაილში shop.txt w რეჟიმით.

ფაილიდან წაიკითხე მხოლოდ პირველი 20 სიმბოლო და დაბეჭდე.

ორი ფაილი, a.txt და b.txt, უნდა გაერთიანდეს. შექმენი ახალი ფაილი merged.txt, სადაც ჯერ იქნება a.txt-ის შიგთავსი, შემდეგ კი b.txt-ის."""

#დავალება 1

with open("names.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        saxeli = input("შეიყვანე სახელი: ")
        f.write(saxeli + "\n")

print("ჩაიწერა!")

#დავალება 2

with open("animals.txt", "r", encoding="utf-8") as f:
    xazebi = f.readlines()

print("ხაზების რაოდენობა:", len(xazebi))
print("პირველი ხაზი:", xazebi[0])

#დავალება 3

shetyobineba = input("შეიყვანე შეტყობინება: ")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(shetyobineba + "\n")

print("დაემატა!")

#დავალება 4

products = ["Bread\n", "Milk\n", "Apple\n", "Juice\n"]

with open("shop.txt", "w", encoding="utf-8") as f:
    f.writelines(products)

print("ჩაიწერა!")


#დავალება 5

with open("shop.txt", "r", encoding="utf-8") as f:
    teksti = f.read(20)

print(teksti)

#დავალება 6

with open("a.txt", "w", encoding="utf-8") as f:
    f.write("ეს არის a.txt\n")

with open("b.txt", "w", encoding="utf-8") as f:
    f.write("ეს არის b.txt\n")

with open("a.txt", "r", encoding="utf-8") as f:
    a_teksti = f.read()

with open("b.txt", "r", encoding="utf-8") as f:
    b_teksti = f.read()

with open("merged.txt", "w", encoding="utf-8") as f:
    f.write(a_teksti)
    f.write(b_teksti)

print("გაერთიანდა!")