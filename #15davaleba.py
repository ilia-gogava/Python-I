"""1. შექმენით lambda ფუნქცია, რომელიც მიიღებს ორ რიცხვს და დააბრუნებს მათ ნამრავლს.

2. გქონდეთ სია რიცხვებით [5, 12, 17, 8, 3, 19, 25]. გამოიყენეთ filter და lambda, რომ გამოიტანოთ მხოლოდ ის რიცხვები, რომლებიც 10-ზე მეტია.

3. შექმენით lambda ფუნქცია, რომელიც რიცხვს შეამოწმებს და დააბრუნებს "დადებითი", "უარყოფითი" ან "ნული".

4. გქონდეთ სია [2, 4, 6, 8, 10]. გამოიყენეთ map და lambda, რომ თითოეული ელემენტი გაამრავლოთ 3-ზე.

5. შექმენით dictionary სამი მათემატიკური ოპერაციით (გამოკლება, გაყოფა, ხარისხში აყვანა), სადაც თითოეული მნიშვნელობა იქნება lambda ფუნქცია. შემდეგ გამოიყენეთ ისინი რიცხვებზე 20 და 4.

6. გქონდეთ სია სტუდენტებით: [("გიორგი", 85), ("ანა", 92), ("ლუკა", 78), ("მარიამ", 95)]. დაალაგეთ ისინი ქულების მიხედვით sorted და lambda ფუნქციის გამოყენებით.

7. დაწერეთ რეკურსიული ფუნქცია, რომელიც მიიღებს რიცხვს n და დააბრუნებს პირველი n ნატურალური რიცხვის ჯამს. მაგალითად, თუ n არის 5, პასუხი უნდა იყოს 15 (1+2+3+4+5).

8. დაწერეთ რეკურსიული ფუნქცია, რომელიც მიიღებს რიცხვს და დააბრუნებს მის ციფრების ჯამს. მაგალითად, 345 არის 12 (3+4+5).

9. დაწერეთ რეკურსიული ფუნქცია, რომელიც მიიღებს სიას და დააბრუნებს მისი ყველა ელემენტის ჯამს. არ გამოიყენოთ sum ფუნქცია.

10. დაწერეთ რეკურსიული ფუნქცია, რომელიც მიიღებს ორ რიცხვს (a და b) და დააბრუნებს a-ს ხარისხად b-ში აყვანას. არ გამოიყენოთ ** ოპერატორი. მაგალითად, power(2, 3) უნდა დააბრუნოს 8."""


#დავალება 1
namravli = lambda a, b: a * b

print(namravli(3, 4))

#დავალება 2
ricxvebi = [5, 12, 17, 8, 3, 19, 25]

shedegi = list(filter(lambda x: x > 10, ricxvebi))

print(shedegi)

#დავალება 3
shemowmeba = lambda x: "დადებითი" if x > 0 else "უარყოფითი" if x < 0 else "ნული"

print(shemowmeba(5))
print(shemowmeba(-3))
print(shemowmeba(0))


#დავალება 4
ricxvebi = [2, 4, 6, 8, 10]

shedegi = list(map(lambda x: x * 3, ricxvebi))

print(shedegi)


#დავალება 5

operaciebi = {
    "gamokhleba": lambda a, b: a - b,
    "gayofa": lambda a, b: a / b,
    "xarishxi": lambda a, b: a ** b
}

print("გამოკლება:", operaciebi["gamokhleba"](20, 4))
print("გაყოფა:", operaciebi["gayofa"](20, 4))
print("ხარისხი:", operaciebi["xarishxi"](20, 4))



#დავალება 6

students = [("გიორგი", 85), ("ანა", 92), ("ლუკა", 78), ("მარიამ", 95)]

dasortirebi = sorted(students, key=lambda x: x[1], reverse=True)

print(dasortirebi)


#დავალება 7
def jami(n):
    if n == 1:
        return 1
    return n + jami(n - 1)

print(jami(5))

#დავალება 8
def cifrebis_jami(n):
    if n < 10:
        return n
    return n % 10 + cifrebis_jami(n // 10)

print(cifrebis_jami(345))

#დავალება 9
def sias_jami(sia):
    if len(sia) == 0:
        return 0
    return sia[0] + sias_jami(sia[1:])

print(sias_jami([1, 2, 3, 4, 5]))


#დავალება 10

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 3))
print(power(20, 4))
