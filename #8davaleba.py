"""1)დაწერეთ პროგრამა, რომელიც დაბეჭდავს გამრავლების ტაბულას 1-დან 10-მდე, მაგრამ მხოლოდ ლუწი შედეგები, ანუ:

2    4    6       8    10
4    8    12    16    20
და ასე

2)დაწერეთ პროგრამა, რომელიც დაბეჭდავს ასეთ ქსელს:
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9

3)students = ["Giorgi", "Ana", "Nikoloz"] languages = ["Python", "JavaScript", "Java"]. დაბეჭდეთ ყველა შესაძლო კომბინაცია.

4)დაწერეთ პროგრამა, რომელიც დაბეჭდავს ყველა კოორდინატს (x, y) სადაც
- x არის 0-დან 11-მდე
- y არის 0-დან 11-მდე

ბონუს-დამატებითი სავარჯიშო:

დაწერეთ პროგრამა, რომელიც ქმნის 8x8 ჭადრაკის დაფას:
# - # - # - # -
- # - # - # - #
# - # - # - # -
- # - # - # - #
# - # - # - # -
- # - # - # - #
# - # - # - # -
- # - # - # - #"""


#დავალება 1

for i in range(1, 11):
    for j in range(1, 11):
        shedegi = i * j
        if shedegi % 2 == 0:
            print(shedegi, end="    ")
    print()

#დავალება 2

for i in range(1, 6):
    for j in range(i, i + 5):
        print(j, end=" ")
    print()


#დავალება 3

students = ["Giorgi", "Ana", "Nikoloz"]
languages = ["Python", "JavaScript", "Java"]

for student in students:
    for language in languages:
        print(student, "-", language)

#დავალება 4

for x in range(0, 12):
    for y in range(0, 12):
        print("("+str(x)+","+str(y)+")", end=" ")
    print()
