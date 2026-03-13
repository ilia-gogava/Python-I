"""
#18 დავალება

ამოცანა 1
დაწერე კლასი Student რომელსაც ექნება name და grade ატრიბუტები. შექმენი ორი Student ობიექტი, დაბეჭდე მათი მონაცემები, შემდეგ ერთ სტუდენტს grade გაზარდე 5-ით და ისევ დაბეჭდე

ამოცანა 2
დაწერე კლასი MathTool რომელსაც ექნება მეთოდები add sub mul div. შექმენი ობიექტი და შეასრულე მინიმუმ ოთხი სხვადასხვა გამოთვლა

ამოცანა 3
დაწერე კლასი MusicBox რომელსაც ექნება box_name და songs სია. დაამატე რამდენიმე სიმღერა, წაშალე ერთი და ბოლოს ყველა დარჩენილი სიმღერა დაბეჭდე

ამოცანა 4
დაწერე კლასი Creature რომელსაც ექნება name ატრიბუტი და say_name მეთოდი. შექმენი მისგან შვილობილი კლასები Wolf და Bird საკუთარი მეთოდებით. შექმენი ობიექტები და გამოიძახე მათი მეთოდები

ამოცანა 5
დაწერე კლასი Person რომელსაც ექნება name age და city. შექმენი ობიექტი, გაზარდე age 1-ით, შემდეგ წაშალე city და სცადე მისი დაბეჭდვა


"""

#1

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("გიორგი", 85)
s2 = Student("ანა", 90)

print(s1.name, s1.grade)
print(s2.name, s2.grade)

s1.grade = s1.grade + 5

print(s1.name, s1.grade)

#2
class MathTool:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

m = MathTool()

print(m.add(10, 5))
print(m.sub(10, 5))
print(m.mul(10, 5))
print(m.div(10, 5))


#3

class MusicBox:
    def __init__(self, box_name):
        self.box_name = box_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def show_songs(self):
        for song in self.songs:
            print(song)

mb = MusicBox("ჩემი პლეილისტი")
mb.add_song("Bohemian Rhapsody")
mb.add_song("Thriller")
mb.add_song("Imagine")
mb.remove_song("Thriller")
mb.show_songs()

#4
class Creature:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("ჩემი სახელია:", self.name)


class Wolf(Creature):
    def howl(self):
        print(self.name, "- აუუუუუ!")


class Bird(Creature):
    def fly(self):
        print(self.name, "- ფრინავს!")


w = Wolf("მგელი")
b = Bird("არწივი")

w.say_name()
w.howl()
b.say_name()
b.fly()


#5

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

p = Person("ილია", 14, "თბილისი")

p.age = p.age + 1
print(p.age)

del p.city

try:
    print(p.city)
except AttributeError:
    print("შეცდომა! city წაშლილია!")


