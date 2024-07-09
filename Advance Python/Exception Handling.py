
#Case 1 Basic Exception Handling

print("\n")

print("Enter the value of Numerator")

num = int(input())

print("Enter the value of Denominator")

den = int(input())

try:

    result = num/den

    print(result)

except ZeroDivisionError:

    print("Exception Handled Successfully!!")

import math

#Case 2 Square Root of a negative number

print("Enter any number of your choice")

a = int(input())

try:

    sqrt = math.sqrt(a)

    print(sqrt)

except:

    print("Square Root of a Negative Number can't be calculated!")

#Case 3 Number With String Exception

print("Enter any random name")

name = str(input())

try:
    new_Name = 10 + name

except TypeError:
    print("String can't be appended with Number")

#Case 4 Name Error

print("Enter a name")

try:
    print("Your name is "+your_name)
except NameError:
    print("Your name is not initialised")


#Case 5 Exception Object

print("Enter any random name")

name = str(input())

try:
    new_Name = 10 + name

except TypeError as t:
    print("String can't be appended with Number "+str(t))