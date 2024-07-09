
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