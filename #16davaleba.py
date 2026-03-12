"""https://www.w3schools.com/python/python_strings_methods.asp 

წაიკითხეთ, გაიაზრეთ და გადაიტანეთ თქვენს პაიჩარმში თითოეული ფუნქციის მაგალითი.

ასევე გააკეთეთ შემდეგი ამოცანები აიასოფტზე:

https://www.aiasoft.ge/problem/138

https://www.aiasoft.ge/problem/207

https://www.aiasoft.ge/problem/247

https://www.aiasoft.ge/problem/414"""


#string Methods - ყველა ფუნქცია

s = "  Hello World  "

# ჰარების მოჭრა
print(s.strip())        # "Hello World"
print(s.lstrip())       # "Hello World  "
print(s.rstrip())       # "  Hello World"

# რეგისტრი
print(s.upper())        # "  HELLO WORLD  "
print(s.lower())        # "  hello world  "
print(s.swapcase())     # "  hELLO wORLD  "
print(s.capitalize())   # "  hello world  " (პირველი დიდი)
print(s.title())        # "  Hello World  " (ყოველი სიტყვა დიდით)

# ძებნა
print(s.find("World"))      # 8 (სად არის)
print(s.count("l"))         # 3 (რამდენჯერ)
print(s.startswith("  H"))  # True
print(s.endswith("  "))     # True
print(s.index("World"))     # 8

# შეცვლა და გაყოფა
print(s.replace("World", "Python"))  # "  Hello Python  "
print("a,b,c".split(","))            # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))     # "a-b-c"

# შემოწმება
print("abc".isalpha())    # True - მხოლოდ ასოები
print("123".isdigit())    # True - მხოლოდ ციფრები
print("abc123".isalnum()) # True - ასო ან ციფრი
print("   ".isspace())    # True - მხოლოდ ჰარი
print("Hello World".istitle())  # True
print("hello".islower())  # True
print("HELLO".isupper())  # True

# სხვა
print("5".zfill(4))          # "0005" - ნულებით შევსება
print("hi".center(10, "*"))  # "****hi****"
print("hi".ljust(10, "-"))   # "hi--------"
print("hi".rjust(10, "-"))   # "--------hi"