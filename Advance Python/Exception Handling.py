
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

#Case 2