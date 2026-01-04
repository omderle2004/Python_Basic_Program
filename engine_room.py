# Basic variables and data types
dumy = "hello Ai leela"
print(dumy)
print(type(dumy))

A = 10
B = 2.5
print(type(A))
print(type(B))

# Arithmetic operations
print(A + B, A - B, A * B, A / B, A // B)
print(A + B - A * B)
print((A + B) * (A - B))

# Comparison operators
print(2 == 2)
print(2 == 3)
print(A != B)
print(A > B)
print(A < B)
print(A >= B)
print(A >= B)
print(A <= B)

# Boolean and string operations
val = True
name = input("enter your name:")
print(name)
print(name.upper())
print(name.lower())
print(name.find('o'))
print(name.replace('o', 'v'))

# Assignment operators
print(A)
A += 2
A *= 4
A -= 2
print(A)

# Logical operators
print(True and False)
print(True & False)
print(True or False)
print(True | False)
print(0 & 1)
print(not True)

# Logical expressions
x = 5
print(x > 3 or x < 4)

x = 5
print(not (x > 3 and x < 10))

# Round function
print(round(3.45))
print(round(-3.95))

# String concatenation
num1 = 'Hello'
num2 = '5'
print(num1 + num2)

# Type conversion
num = 2.0
print(type(num))
num = str(num)
print(type(num))

# Positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# Even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Grade calculation
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

# -------------------- LIST CREATION --------------------
numbers = [10, 20, 30, 40, 50]
names = ["Om", "Amit", "Riya"]

print(numbers)
print(names)
print(type(numbers))


# -------------------- ACCESSING ELEMENTS --------------------
nums = [5, 10, 15, 20]
print(nums[0])
print(nums[2])
print(nums[-1])


# -------------------- MODIFYING ELEMENTS --------------------
nums = [1, 2, 3, 4]
nums[1] = 10
print(nums)


# -------------------- LENGTH OF LIST --------------------
nums = [10, 20, 30, 40]
print(len(nums))


# -------------------- ADDING ELEMENTS --------------------
nums = [1, 2, 3]
nums.append(4)
nums.insert(1, 10)
print(nums)


# -------------------- REMOVING ELEMENTS --------------------
nums = [10, 20, 30, 40]
nums.remove(20)
nums.pop()
nums.pop(0)
print(nums)


# -------------------- LOOP THROUGH LIST --------------------
fruits = ["apple", "banana", "mango"]
for item in fruits:
    print(item)


# -------------------- CHECK ELEMENT IN LIST --------------------
nums = [5, 10, 15]
print(10 in nums)
print(20 in nums)


# -------------------- LIST SLICING --------------------
nums = [1, 2, 3, 4, 5]
print(nums[1:4])
print(nums[:3])
print(nums[::2])


# -------------------- SORTING LIST --------------------
nums = [40, 10, 30, 20]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


# -------------------- SUM, MAX, MIN --------------------
nums = [10, 20, 30]
print(sum(nums))
print(max(nums))
print(min(nums))


# -------------------- COUNT EVEN NUMBERS --------------------
nums = [1, 2, 3, 4, 5, 6]
count = 0
for n in nums:
    if n % 2 == 0:
        count += 1
print("Even numbers count:", count)


# -------------------- FIND LARGEST ELEMENT --------------------
nums = [10, 25, 5, 40, 15]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest number:", largest)

# -------------------- INSERT IN LIST --------------------
nums = [10, 20, 30, 40]
nums.insert(2, 25)
print(nums)


# -------------------- MULTIPLE INSERT OPERATIONS --------------------
values = [1, 2, 3]
values.insert(0, 100)
values.insert(2, 200)
values.insert(len(values), 300)
print(values)


# -------------------- BASIC NESTED LIST --------------------
nested = [[1, 2, 3], [4, 5, 6]]
print(nested)


# -------------------- ACCESS NESTED LIST ELEMENTS --------------------
print(nested[0])
print(nested[1])
print(nested[0][1])
print(nested[1][2])


# -------------------- MODIFY NESTED LIST --------------------
nested[0][1] = 20
nested[1][2] = 60
print(nested)


# -------------------- LOOP THROUGH NESTED LIST --------------------
matrix = [[1, 2, 3], [4, 5, 6]]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


# -------------------- ADD ELEMENT TO NESTED LIST --------------------
matrix.append([7, 8, 9])
matrix[0].append(10)
print(matrix)


# -------------------- SUM OF ALL ELEMENTS IN NESTED LIST --------------------
total = 0
for row in matrix:
    for item in row:
        total += item
print("Sum:", total)

# -------------------- TUPLE CREATION --------------------
tup = (10, 20, 30, 40)
print(tup)
print(type(tup))


# -------------------- SINGLE ELEMENT TUPLE --------------------
single = (50,)
print(single)
print(type(single))


# -------------------- ACCESSING TUPLE ELEMENTS --------------------
nums = (5, 10, 15, 20)
print(nums[0])
print(nums[2])
print(nums[-1])


# -------------------- TUPLE SLICING --------------------
nums = (1, 2, 3, 4, 5)
print(nums[1:4])
print(nums[:3])
print(nums[::2])


# -------------------- LOOP THROUGH TUPLE --------------------
fruits = ("apple", "banana", "mango")
for item in fruits:
    print(item)


# -------------------- CHECK ELEMENT IN TUPLE --------------------
nums = (10, 20, 30)
print(20 in nums)
print(40 in nums)


# -------------------- BASIC TUPLE FUNCTIONS --------------------
nums = (10, 20, 10, 30)
print(nums.count(10))
print(nums.index(20))
# -------------------- BASIC TUPLE INDEXING --------------------
tup = (10, 20, 30, 40, 50)
print(tup[0])
print(tup[2])
print(tup[-1])
print(tup[-3])


# -------------------- TUPLE SLICING WITH INDEXES --------------------
tup = (1, 2, 3, 4, 5, 6)
print(tup[1:4])
print(tup[:3])
print(tup[3:])
print(tup[-4:-1])


# -------------------- STEP INDEXING --------------------
tup = (10, 20, 30, 40, 50, 60)
print(tup[::2])
print(tup[1::2])
print(tup[::-1])


# -------------------- FIND INDEX OF ELEMENT --------------------
tup = (5, 10, 15, 20)
print(tup.index(10))
print(tup.index(20))


# -------------------- COUNT USING INDEX POSITION --------------------
tup = (10, 20, 10, 30, 10)
print(tup.count(10))


# -------------------- LOOP WITH INDEX --------------------
tup = ("a", "b", "c", "d")
for i in range(len(tup)):
    print("Index", i, "Value", tup[i])


# -------------------- ENUMERATE WITH TUPLE --------------------
tup = (100, 200, 300)
for index, value in enumerate(tup):
    print(index, value)


# -------------------- NESTED TUPLE INDEXING --------------------
nested = ((1, 2, 3), (4, 5, 6))
print(nested[0])
print(nested[1][2])
# -------------------- DICTIONARY CREATION --------------------
student = {
    "name": "Om",
    "age": 21,
    "branch": "AI&DS"
}
print(student)
print(type(student))


# -------------------- ACCESS DICTIONARY VALUES --------------------
print(student["name"])
print(student.get("age"))


# -------------------- MODIFY & ADD ELEMENTS --------------------
student["age"] = 22
student["college"] = "KKW"
print(student)


# -------------------- REMOVE ELEMENTS --------------------
student.pop("college")
print(student)


# -------------------- DICTIONARY FUNCTIONS --------------------
print(student.keys())
print(student.values())
print(student.items())


# -------------------- CHECK KEY EXISTENCE --------------------
print("name" in student)
print("marks" in student)


# -------------------- LOOP THROUGH DICTIONARY (KEYS) --------------------
for key in student:
    print(key)


# -------------------- LOOP THROUGH DICTIONARY (VALUES) --------------------
for value in student.values():
    print(value)


# -------------------- LOOP THROUGH DICTIONARY (KEY-VALUE) --------------------
for key, value in student.items():
    print(key, ":", value)


# -------------------- NESTED DICTIONARY --------------------
students = {
    "student1": {
        "name": "Om",
        "age": 21
    },
    "student2": {
        "name": "Amit",
        "age": 22
    }
}
print(students)


# -------------------- ACCESS NESTED DICTIONARY --------------------
print(students["student1"])
print(students["student1"]["name"])


# -------------------- LOOP THROUGH NESTED DICTIONARY --------------------
for key, value in students.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(sub_key, ":", sub_value)
# -------------------- CREATE EMPTY DICTIONARY --------------------
d = {}
print(d)


# -------------------- UPDATE DICTIONARY --------------------
d.update({"a": 1, "b": 2})
print(d)


# -------------------- COPY DICTIONARY --------------------
d1 = d.copy()
print(d1)


# -------------------- CLEAR DICTIONARY --------------------
temp = {"x": 10, "y": 20}
temp.clear()
print(temp)


# -------------------- DEFAULT VALUE USING GET --------------------
student = {"name": "Om", "age": 21}
print(student.get("marks", "Not Found"))


# -------------------- FROMKEYS FUNCTION --------------------
keys = ("id", "name", "branch")
default_dict = dict.fromkeys(keys, "NA")
print(default_dict)


# -------------------- SETDEFAULT FUNCTION --------------------
data = {"name": "Om"}
data.setdefault("age", 20)
data.setdefault("name", "Amit")
print(data)


# -------------------- COUNT FREQUENCY OF ELEMENTS --------------------
nums = [1, 2, 2, 3, 3, 3]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)


# -------------------- MERGE TWO DICTIONARIES --------------------
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}
print(merged)


# -------------------- DICTIONARY COMPREHENSION --------------------
squares = {x: x*x for x in range(1, 6)}
print(squares)


# -------------------- NESTED DICTIONARY UPDATE --------------------
students = {
    "s1": {"name": "Om", "age": 21},
    "s2": {"name": "Amit", "age": 22}
}
students["s1"]["age"] = 23
print(students)


# -------------------- LOOP THROUGH NESTED DICTIONARY --------------------
for s_id, info in students.items():
    print("ID:", s_id)
    for key, value in info.items():
        print(key, ":", value)

# -------------------- SET CREATION --------------------
s1 = {1, 2, 3, 4}
s2 = {"apple", "banana", "mango"}
s3 = {1, 2, 2, 3, 3}

print(s1)
print(s2)
print(s3)
print(type(s1))


# -------------------- EMPTY SET --------------------
empty_set = set()
print(empty_set)


# -------------------- ADD ELEMENTS --------------------
nums = {1, 2, 3}
nums.add(4)
nums.update([5, 6])
print(nums)


# -------------------- REMOVE ELEMENTS --------------------
nums.remove(2)
nums.discard(10)
nums.pop()
print(nums)


# -------------------- SET OPERATIONS --------------------
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


# -------------------- CHECK MEMBERSHIP --------------------
print(2 in a)
print(10 in a)


# -------------------- LOOP THROUGH SET --------------------
fruits = {"apple", "banana", "mango"}
for item in fruits:
    print(item)


# -------------------- SET FUNCTIONS --------------------
nums = {10, 20, 30}
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))


# -------------------- COPY AND CLEAR --------------------
s = {1, 2, 3}
s_copy = s.copy()
s.clear()
print(s_copy)
print(s)


# -------------------- SUBSET AND SUPERSET --------------------
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))
print(b.issuperset(a))


# -------------------- FROZENSET --------------------
fs = frozenset([1, 2, 3])
print(fs)

# -------------------- CREATE SET FROM USER INPUT --------------------
n = int(input("Enter number of elements: "))
s = set()

for i in range(n):
    s.add(int(input("Enter element: ")))

print(s)


# -------------------- ADD AND REMOVE ELEMENT --------------------
num = int(input("Enter element to add: "))
s.add(num)

num = int(input("Enter element to remove: "))
s.discard(num)

print(s)


# -------------------- CHECK ELEMENT IN SET --------------------
x = int(input("Enter element to check: "))
if x in s:
    print("Element found")
else:
    print("Element not found")


# -------------------- UNION OF TWO SETS --------------------
n1 = int(input("Enter size of first set: "))
set1 = set()

for i in range(n1):
    set1.add(int(input("Enter element: ")))

n2 = int(input("Enter size of second set: "))
set2 = set()

for i in range(n2):
    set2.add(int(input("Enter element: ")))

print("Union:", set1 | set2)


# -------------------- INTERSECTION OF TWO SETS --------------------
print("Intersection:", set1 & set2)


# -------------------- DIFFERENCE OF TWO SETS --------------------
print("Difference (set1 - set2):", set1 - set2)


# -------------------- CHECK SUBSET --------------------
if set1.issubset(set2):
    print("Set1 is subset of Set2")
else:
    print("Set1 is not subset of Set2")


# -------------------- FIND MAX AND MIN --------------------
if s:
    print("Max:", max(s))
    print("Min:", min(s))

# -------------------- SIMPLE FUNCTION --------------------
def greet():
    print("Hello, Welcome to Python")

greet()


# -------------------- FUNCTION WITH PARAMETERS --------------------
def add(a, b):
    print("Sum:", a + b)

add(10, 20)


# -------------------- FUNCTION WITH RETURN VALUE --------------------
def square(n):
    return n * n

result = square(5)
print("Square:", result)


# -------------------- FUNCTION WITH USER INPUT --------------------
def multiply(a, b):
    return a * b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Multiplication:", multiply(x, y))


# -------------------- DEFAULT ARGUMENT FUNCTION --------------------
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(5, 3))


# -------------------- KEYWORD ARGUMENT FUNCTION --------------------
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=21, name="Om")


# -------------------- FUNCTION CALLING FUNCTION --------------------
def outer():
    print("Outer function")
    inner()

def inner():
    print("Inner function")

outer()


# -------------------- CHECK EVEN OR ODD USING FUNCTION --------------------
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(check_even(num))
# -------------------- BASIC FOR LOOP --------------------
for i in range(1, 6):
    print(i)


# -------------------- FOR LOOP WITH LIST --------------------
nums = [10, 20, 30, 40]
for n in nums:
    print(n)


# -------------------- FOR LOOP WITH STRING --------------------
name = "Python"
for ch in name:
    print(ch)


# -------------------- FOR LOOP WITH USER INPUT --------------------
n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(i)


# -------------------- FOR LOOP WITH STEP --------------------
for i in range(0, 11, 2):
    print(i)


# -------------------- NESTED FOR LOOP --------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# -------------------- NESTED LOOP WITH STAR PATTERN --------------------
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# -------------------- MULTIPLICATION TABLE --------------------
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -------------------- MATRIX USING NESTED LOOP --------------------
matrix = [[1, 2, 3], [4, 5, 6]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
# -------------------- PRINT NUMBERS --------------------
for i in range(1, 6):
    print(i)


# -------------------- SUM OF FIRST N NUMBERS --------------------
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)


# -------------------- PRINT EVEN NUMBERS --------------------
for i in range(2, 11, 2):
    print(i)


# -------------------- LOOP THROUGH LIST --------------------
nums = [10, 20, 30, 40]
for n in nums:
    print(n)


# -------------------- MULTIPLICATION TABLE --------------------
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -------------------- BASIC NESTED LOOP --------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# -------------------- STAR PATTERN --------------------
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# -------------------- NUMBER PATTERN --------------------
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# -------------------- MATRIX DISPLAY --------------------
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
# -------------------- BASIC WHILE LOOP --------------------
i = 1
while i <= 5:
    print(i)
    i += 1


# -------------------- SUM OF FIRST N NUMBERS --------------------
n = int(input("Enter n: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum:", total)


# -------------------- PRINT EVEN NUMBERS --------------------
i = 2
while i <= 10:
    print(i)
    i += 2


# -------------------- MULTIPLICATION TABLE --------------------
num = int(input("Enter number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# -------------------- LOOP THROUGH LIST --------------------
nums = [10, 20, 30, 40]
i = 0

while i < len(nums):
    print(nums[i])
    i += 1


# -------------------- REVERSE A NUMBER --------------------
num = int(input("Enter number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number:", rev)


# -------------------- FACTORIAL USING WHILE --------------------
n = int(input("Enter number: "))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial:", fact)
# -------------------- CHECK PRIME NUMBER --------------------
num = int(input("Enter number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime number")
else:
    print("Not a prime number")


# -------------------- FIBONACCI SERIES --------------------
n = int(input("Enter terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# -------------------- PALINDROME NUMBER --------------------
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# -------------------- ARMSTRONG NUMBER --------------------
num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")


# -------------------- COUNT VOWELS IN STRING --------------------
text = input("Enter string: ")
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Vowel count:", count)


# -------------------- FUNCTION TO CHECK EVEN OR ODD --------------------
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number: "))
print(even_odd(num))
# -------------------- BASIC CLASS AND OBJECT --------------------
class Student:
    def display(self):
        print("This is a Student class")

s1 = Student()
s1.display()


# -------------------- CLASS WITH VARIABLES --------------------
class Person:
    name = "Om"
    age = 21

p1 = Person()
print(p1.name)
print(p1.age)


# -------------------- CONSTRUCTOR (__init__) --------------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Om", 21)
s2 = Student("Amit", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)


# -------------------- CLASS WITH METHODS --------------------
class Calculator:
    def add(self, a, b):
        print("Sum:", a + b)

    def sub(self, a, b):
        print("Subtraction:", a - b)

c = Calculator()
c.add(10, 5)
c.sub(10, 5)


# -------------------- OBJECT WITH USER INPUT --------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

name = input("Enter name: ")
salary = int(input("Enter salary: "))

e1 = Employee(name, salary)
e1.show()


# -------------------- MULTIPLE OBJECTS --------------------
class Car:
    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = Car("Audi")

print(c1.brand)
print(c2.brand)

# -------------------- WHAT IS MODULE --------------------
# A module is a file that contains Python code (functions, variables, classes)
# Example: math, random, datetime


# -------------------- IMPORT MATH MODULE --------------------
import math


# -------------------- BASIC MATH FUNCTIONS --------------------
print(math.sqrt(25))
print(math.pow(2, 3))
print(math.factorial(5))


# -------------------- CEIL AND FLOOR --------------------
print(math.ceil(3.2))
print(math.floor(3.8))


# -------------------- PI AND E CONSTANTS --------------------
print(math.pi)
print(math.e)


# -------------------- ABSOLUTE VALUE --------------------
print(abs(-10))


# -------------------- TRIGONOMETRIC FUNCTIONS --------------------
print(math.sin(math.radians(30)))
print(math.cos(math.radians(60)))
print(math.tan(math.radians(45)))


# -------------------- LOGARITHMIC FUNCTIONS --------------------
print(math.log(10))
print(math.log10(100))
print(math.log2(8))


# -------------------- GCD AND LCM --------------------
print(math.gcd(12, 18))
print(math.lcm(12, 18))


# -------------------- ROUNDING FUNCTIONS --------------------
print(round(3.6))
print(round(3.14159, 2))


# -------------------- CHECK NAN AND INFINITY --------------------
print(math.isnan(10.5))
print(math.isinf(10))


# -------------------- IMPORT SPECIFIC FUNCTIONS --------------------
from math import sqrt, pi
print(sqrt(36))
print(pi)


# -------------------- USER INPUT WITH MATH MODULE --------------------
num = int(input("Enter number: "))
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))

# -------------------- IMPORT DATETIME MODULE --------------------
import datetime


# -------------------- CURRENT DATE AND TIME --------------------
now = datetime.datetime.now()
print(now)


# -------------------- CURRENT DATE ONLY --------------------
today = datetime.date.today()
print(today)


# -------------------- CURRENT TIME ONLY --------------------
current_time = datetime.datetime.now().time()
print(current_time)


# -------------------- CREATE CUSTOM DATE --------------------
d = datetime.date(2025, 1, 1)
print(d)


# -------------------- CREATE CUSTOM DATE & TIME --------------------
dt = datetime.datetime(2025, 1, 1, 10, 30, 0)
print(dt)


# -------------------- ACCESS DATE ATTRIBUTES --------------------
print(today.year)
print(today.month)
print(today.day)


# -------------------- ACCESS TIME ATTRIBUTES --------------------
print(now.hour)
print(now.minute)
print(now.second)


# -------------------- FORMAT DATE AND TIME --------------------
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)


# -------------------- STRING TO DATE --------------------
date_str = "01-01-2025"
date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print(date_obj)


# -------------------- DATE DIFFERENCE --------------------
d1 = datetime.date(2025, 1, 1)
d2 = datetime.date.today()
diff = d2 - d1
print("Days difference:", diff.days)


# -------------------- ADD OR SUBTRACT DAYS --------------------
new_date = today + datetime.timedelta(days=10)
old_date = today - datetime.timedelta(days=5)
print(new_date)
print(old_date)
