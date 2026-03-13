"""ამოცანა 1 – პროდუქტის საწყობი
შექმენი კლასი Product, რომელსაც აქვს name, price და amount. დაამატე მეთოდი sell(qty), რომელიც ამცირებს amount-ს. თუ გაყიდვა შეუძლებელია (არ ჰყოფნის), დაბეჭდოს “Not enough product”. შექმენი ობიექტი და სცადე სხვადასხვა რაოდენობის გაყიდვა.

ამოცანა 2 – User და Admin მემკვიდრეობა
შექმენი კლასი User(name). დაამატე მეთოდი info(), რომელიც ბეჭდავს “User: <name>”. შემდეგ შექმენი Admin(User), რომელსაც info() მეთოდი გადაფარებული ექნება და ბეჭდავს “Admin: <name>”. შექმენი ორივე ობიექტი და გამოიძახე info().

ამოცანა 3 – ბანკის ანგარიში private ბალანსით
შექმენი კლასი BankAccount, რომელსაც აქვს private ცვლადი __balance. დაამატე deposit(amount), withdraw(amount) და get_balance(). ფულზე გატანა მხოლოდ იმ შემთხვევაში იყოს შესაძლებელი, თუ თანხა საკმარისია. შექმენი ობიექტი, შეიტანე და გამოიტანე ფული.

ამოცანა 4 – Geometry ფიგურები (მემკვიდრეობა და მეთოდების გადაფარვა)
შექმენი მშობელი კლასი Shape, რომელსაც აქვს მეთოდი area(), რომელიც უბრალოდ აბრუნებს 0-ს. შექმენი შვილები:
Rectangle(width, height) – area() აბრუნებს სიგანესიმაღლეს
Circle(radius) – area() აბრუნებს πr*r (გამოიყენე 3.14)
შექმენი თითო ობიექტი და დაბეჭდე ფართობები.

ამოცანა 5 – მაღაზიის კალათა
შექმენი კლასი Cart, რომელსაც აქვს items (სია). დაამატე add_item(item) და total_price() – რომელიც შეაჯამებს ყველა item-ის price-ს. სასარგებლოდ შექმენი დამატებითი კლასი Item(name, price). დაამატე 3 different item კალათაში და გამოთვალე ჯამი.

ამოცანა 6 – უნივერსიტეტი და სტუდენტები (ობიექტების სია კლასში)
შექმენი კლასი Student(name, gpa). შემდეგ შექმენი კლასი University, რომელსაც აქვს students (სია) და add_student(stud) და best_student(), რომელიც აბრუნებს უმაღლესი gpa-ს მქონე სტუდენტის სახელს. დაამატე 3 სტუდენტი და მოძებნე საუკეთესო"""

#1
class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def sell(self, qty):
        if qty > self.amount:
            print("Not enough product")
        else:
            self.amount = self.amount - qty
            print("გაიყიდა:", qty, "| დარჩა:", self.amount)

p = Product("ვაშლი", 2.5, 10)

p.sell(3)
p.sell(5)
p.sell(10)

#2

class User:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("User:", self.name)


class Admin(User):
    def info(self):
        print("Admin:", self.name)

u = User("გიორგი")
a = Admin("ილია")

u.info()
a.info()


#3

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("შეტანილია:", amount)
        else:
            print("შეცდომა! თანხა დადებითი უნდა იყოს!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("არ ჰყოფნის თანხა!")
        else:
            self.__balance = self.__balance - amount
            print("გამოტანილია:", amount)

    def get_balance(self):
        print("ბალანსი:", self.__balance)

b = BankAccount()

b.deposit(1000)
b.withdraw(300)
b.withdraw(800)
b.get_balance()


#4

class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(5, 3)
c = Circle(4)

print("მართკუთხედის ფართობი:", r.area())
print("წრის ფართობი:", c.area())

#5

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("დაემატა:", item.name, item.price)

    def total_price(self):
        total = 0
        for item in self.items:
            total = total + item.price
        return total

cart = Cart()

cart.add_item(Item("ვაშლი", 3.0))
cart.add_item(Item("პური", 2.5))
cart.add_item(Item("წყალი", 1.5))

print("ჯამი:", cart.total_price())

#6

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


class University:
    def __init__(self):
        self.students = []

    def add_student(self, stud):
        self.students.append(stud)
        print("დაემატა:", stud.name)

    def best_student(self):
        best = self.students[0]
        for s in self.students:
            if s.gpa > best.gpa:
                best = s
        return best.name

uni = University()

uni.add_student(Student("გიორგი", 3.5))
uni.add_student(Student("ანა", 3.9))
uni.add_student(Student("ლუკა", 3.7))

print("საუკეთესო სტუდენტი:", uni.best_student())

