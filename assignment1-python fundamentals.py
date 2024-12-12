
#exercise1
"""Write Python code that prints your name, student number and email address.
An example runs of the program:  """
from locale import currency

print("""hanan pv
7698xxxx56
hanananu578@gmail.com""")

#Exercise 2
#Write Python code that prints your name, student number and email address using escape sequences.

print("hanan pv \n 7698xxxx56\n hanananu578@gmail,com")

#Exercise 3
#Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.

a=14
b=7
print(f"sum of {a} and {b} is {a+b}")
print(f"difference of {a} and {b} is {a-b}")
print(f"multiplication of {a} and {b} is {a*b}")
print(f"division of {a} and {b} is {a/b}")

#Exercise 4
#Write Python code that displays the numbers from 1 to 5 as steps.

i=1
while i<=5:
    print (i)
    i=i+1

#Exercise 5
#Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
#An example runs of the program:
#"SDK" stands for "Software Development Kit", whereas
#"IDE" stands for "Integrated Development Environment".

print('\"SDK\" stands for \"Software Development Kit\", whereas \n \"IDE\"stands for \"integreted Development Envionment\"')

#Exercise 6
#Practice and check the output
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

#Exercise 7
#Define the variables below. Print the types of each variable. What is the sum of your variables?
# (Hint: use a type conversion function.) What datatype is the sum?
num=23
textnum="57"
decimal=98.3
print(type(num))
print(type(textnum))
print(type(decimal))
decimal=int(decimal)
textnum=int(textnum)
SUM=num+textnum+decimal
print(SUM)
print(type(SUM))

#Exercise 8
# calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also.
# Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values
# (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

x=365 #no of days in a year
y=60 #minute in an hour
z=24 #hour in a day

print("total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour")
totalminyear=x*y*z
print(totalminyear,"minutes per year")

# Exercise 9
# Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# An example runs of the program:
# Please enter you name: Tony
# Hi Tony, welcome to Python programming :)

name=input('Enter your name:')
print(f"Hi {name}, welcome to Python programming :)t")

# Exercise 10
# Name your file: PoundsToDollars.py
# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
# An example runs of the program:
# Please enter amount in pounds: XXX
# £ XXX are $ XXX

pounds=float(input('Enter amount in pounds:'))
dollars=pounds*1.2746
print(f"£ {pounds} are $ {dollars}")