"""შექმენით კლასი Car, რომელსაც ექნება კლასის ცვლადი manufacturer და ობიექტის ცვლადი model. შექმენით სამი მანქანის ობიექტი და წარამოაჩინეთ თითოეულის model და საერთო manufacturer.

ამოცანა 2
დაწერეთ კლასი Employee, რომელსაც ექნება public ცვლადი name, protected ცვლადი _position და private ცვლადი __salary. შექმენით მეთოდი, რომელიც გამოიტანს ხელფასს მხოლოდ სწორი კოდის შეყვანის შემთხვევაში.

ამოცანა 3
შექმენით მშობელი კლასი Device, რომელსაც ექნება კონსტრუქტორი brand. ხელშემწყობ კლასში Phone დაამატეთ კონსტრუქტორი brand და model, სადაც brand უნდა გადაეცეს მშობელ კლასს super()–ის გამოყენებით.

ამოცანა 4
დაწერეთ კლასი Student, რომელსაც ექნება private ცვლადი __grade. შექმენით getter და setter მეთოდები, სადაც setter გადაამოწმებს, არის თუ არა მონაცემი 1–დან 10–მდე დიაპაზონში.

ამოცანა 5
შექმენით კლასები Animal და Dog, სადაც Dog მემკვიდრეობით მიიღებს Animal–ს. მშობელ კლასში იქნება მეთოდი sound(), ხოლო შვილ კლასში ეს მეთოდი უნდა გადაფაროთ ისე, რომ ჯერ გამოიძახოს მშობელი მეთოდი, შემდეგ მოახდინოს თავისი ტექსტის დამატება.

ამოცანა 6
დაწერეთ კლასი BankAccount, რომელსაც ექნება private ბალანსი. დაამატეთ მეთოდი deposit(amount), რომელიც თანხას მხოლოდ პოზიტიური რიცხვის შეყვანისას დაამატებს ბალანსში.

ამოცანა 7
შექმენით კლასი Laptop, რომელსაც ექნება public ცვლადი owner და protected ცვლადი _os. შექმენით შვილობილი კლასი GamingLaptop, რომელიც დაამატებს ცვლადს gpu და დაბეჭდავს მთელ ინფორმაციას მშობლის ცვლადების ჩათვლით."""


#1
class Car:
    manufacturer = "Toyota"

    def __init__(self, model):
        self.model = model

c1 = Car("Camry")
c2 = Car("Corolla")
c3 = Car("Yaris")

print(c1.model, Car.manufacturer)
print(c2.model, Car.manufacturer)
print(c3.model, Car.manufacturer)


#2
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self._position = position
        self.__salary = salary

    def show_salary(self, code):
        if code == "1234":
            print("ხელფასი:", self.__salary)
        else:
            print("არასწორი კოდი!")

e = Employee("გიორგი", "მენეჯერი", 3000)

print(e.name)
print(e._position)

e.show_salary("0000")
e.show_salary("1234")


#3
class Device:
    def __init__(self, brand):
        self.brand = brand


class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show(self):
        print("მარკა:", self.brand)
        print("მოდელი:", self.model)

p = Phone("Samsung", "Galaxy S24")
p.show()


#4
class Student:
    def __init__(self):
        self.__grade = None

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 1 <= grade <= 10:
            self.__grade = grade
            print("ქულა დაყენდა:", grade)
        else:
            print("შეცდომა! ქულა უნდა იყოს 1-დან 10-მდე!")

s = Student()

s.set_grade(15)
s.set_grade(8)

print("ქულა:", s.get_grade())


#5
class Animal:
    def sound(self):
        print("ცხოველი ხმას გამოსცემს...")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("ძაღლი: ჰავ ჰავ!")

a = Animal()
d = Dog()

a.sound()
print("---")
d.sound()


#6
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("დაემატა:", amount, "| ბალანსი:", self.__balance)
        else:
            print("შეცდომა! თანხა უნდა იყოს დადებითი!")

    def show_balance(self):
        print("ბალანსი:", self.__balance)

b = BankAccount()

b.deposit(-100)
b.deposit(500)
b.deposit(300)
b.show_balance()


#7
class Laptop:
    def __init__(self, owner, os):
        self.owner = owner
        self._os = os


class GamingLaptop(Laptop):
    def __init__(self, owner, os, gpu):
        super().__init__(owner, os)
        self.gpu = gpu

    def show_info(self):
        print("მფლობელი:", self.owner)
        print("OS:", self._os)
        print("GPU:", self.gpu)

gl = GamingLaptop("ილია", "Windows 11", "RTX 4080")
gl.show_info()
