'''
num = float(input("enter a number: "))

if num > 0:

    print("positive")

elif num < 0:

    print("negative")
else:

    print("zero")
'''

'''
num = int(input("enter a number:"))

if num % 2 == 0:

    print("even")
else:

    print("odd")
'''
'''

a  = 10

b = 20

if a > b:

    print("Greater number is:", a)
else:

    print("Greater number is:", b)
'''
'''

a = 10

b = 20

c = 30

if a > b and a > c:

    print("greatest number is" , a)

elif b > a and b > c:

    print("greatest number is", b)
else:

    print("greatest number is", c)
'''

'''

age = int(input("enter your age:"))

if age >= 18:

    print("you are eligible for voting")
else:

    print("you are not eligible for voting")
'''

'''

year = int(input("enter a year:"))

if year % 400 == 0:

    print("leap year")

elif year % 100 == 0:

    print("not a leap year")

elif year % 4 == 0:

        print ("leap year")
else:

    print("not a leap year")
'''

'''

ch = input("enter a character:")

if ch in 'aeiou':

    print("vowel")
else:

    print("consonant")
'''


'''
num = int(input("enter a number "))


if num % 5 == 0 and num % 11 == 0:

    print ("number is divisible by 5 and 11")
else:

    print("nmuber is not divisible by 5 and 11")
'''

'''
num = int(input("enter a number:"))

if num % 3 == 0 and num % 7 == 0:

    print("multiple of both 3 and 7")
else:
    print("not a multiple of both 3 and 7")
'''


'''
marks = int(input("enter your marks:"))
if marks >= 90 and marks <= 100:
    print("grade A")
elif marks >= 80:
    print("grade B")
elif marks >= 70:
    print("grade C")
elif marks >= 60:
    print("grade D")
else:
    print("invalid marks")
'''

'''
ch = input("enter a character: ")

if ch.isupper():
    print("uppercase")
elif ch.islower():
    print("lowercase")
else:
    pirnt("not an alphabet")
'''

'''
ch = input("enter an alphabet: ")
if ch == 'a':
    print("vowel")
elif ch == 'e':
    print("vowel")
elif ch == 'i':
    print("vowel")
elif ch == 'o':
    print("vowel")
elif ch == 'u':
    print("vowel")
else:
    print("consonant")
'''

'''
a = int(input("enter frist side:"))
b = int(input("emter second side:"))
c = int(input("enter third side:"))

if a + b > a + c > b and b + c > a:
    print("tringle can be formed")
else:
    print("tringle connot be formed")
'''

'''
units = int(input("enter electricity units:"))

if units < 0:
    print("invalid units")
elif units <= 100:
    bill = units * 5 
    print("electricity bill =",bill)
elif units <=200:
    bill = 100 * 5 + (units - 100) *7
    print("electricity bill =", bill)
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("electricity bill=", bill)
else:
    bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15
    print("electricity bill=",bill)
'''



'''
income = int(input("enter your annual income:"))

if income < 0:
    print("invaild income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) *0.30
if income >= 0:
    print("income tax =",tax)
'''

'''
maths = int(input("enter maths marks:"))
science = int(input("enter science marks:"))
english = int(input("enter english marks: "))

if maths >= 35 and science >= 35 and english >= 35:
    print("student is pass")
else:
    print("student is fail")
'''

'''
num = int(input("enter a number:"))

if num >= 1 and num <= 100:
    print("number is within the range")
else:
    print("number is outside the range")
'''

'''
a = float(input("enter frist number:"))
op = input("enter operator (+,-,*,/):")
b = float(input("enter second number:"))

if op == '+':
   print("result =", a + b)
elif op == '-':
    print("result =", a - b)
elif op == '*':
    print("result =", a * b)
elif op == '/':
    if b != 0:
     print("result =", a / b)
    else:
     print("cannot divide by  zero")
else:
     print("invalid operator")
'''

'''
year = int(input("enter a year:"))

if year % 100 == 0 and year % 400 == 0:
    print("century leap year")
else:
    print("not a century leap year")
'''
'''
month = int(input("enter month number(1-12):"))

if month in [3,4,5]:
    print("summer season")
elif month in [6,7,8,9,]:
    print("rainy season")
elif month in [10,11]:
    print("autumn season")
elif month in [12,1,2]:
    print("winter season")
else:
    print("invalid month number")
'''

'''
month = int(input("enter month number(1-12):"))
year = int(input("enter year:"))

if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
     print("28 days")
elif month in [4,6,9,11]:
    print("30 days")
elif month in [1,3,5,7,8,10,12]:
    print("31 days")
else:
    print("invalid month number")
'''

'''
password = input("enter password:")

if (len(password) >= 8 and any(ch.isdigit() for ch in password) and any(ch.isalpha() for ch in password)):
    print("valid password")
else:
    print("invalid password")
'''


'''
age = int(input("enter your age:"))

if age <5:
    print("ticket is free")
elif age <= 12:
    print("ticket price = Rs. 50")
elif age <= 59:
    print("ticket price = Rs. 100")
else:
    print("ticket price = Rs. 60")
'''

'''
amount = float(input("enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
      disount = amount * 0.10
elif amount >=1000:
      discount = amount * 0.05
else:
    discount = 0
print("Discount =", discount)
print("Final Amount =", amount - discount)
'''
'''
age = int(input("Enter your age: "))
eyesight = input("Is your eyesight normal? (yes/no): ")
if age >= 18 and eyesight == "yes":
    print("Eligible for Driving License")
else:
        print("Not Eligible for Driving License")
'''

'''
username = input("enter username:")
password = input("enter password:")

if username == "charu" and password == "charu123":
    print("login successful")
else:
    print("invalid username or password")
'''

'''
while True:
    print("\na. addition")
    print("b. subraction")
    print("c. multiplication")
    print("d. division")
    print("e. exit")

    choice = input("enter your choice:")
    if choice == "e":
        print("program exited")
        break;

    if choice in ["a", "b", "c", "d"]:
        num1 = float(input("enter frist number:"))
        num2 = float(input("enter second number:"))

        if choice == "a":
            print("addition=", num1 + num2)
        elif choice == "b":
            print("subtraction =", num1 - num2)
        elif choice == "c":
            print("multiplication =", num1 * num2)
        elif choice == "d":
            if num2 != 0:
                print("division =", num1 / num2)
            else:
                print("cannot divide by zero")
    else:
        print("invalid choice"
'''
     

 
