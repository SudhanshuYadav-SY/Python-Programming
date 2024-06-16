print("This is Case 1 where the numbers from 0 to 9 will be printed")
for i in range(10) :
    print(i)

print("This is Case 2 Where we don't want 0 to be printed")
for a in range(1,10) :
    print(a)

print("This is Case 3 where we want numbers in a Specific Range of 4 to 15")
for b in range(4,15) :
    print(b)

print("This is Case 4 where we want numbers with specific steps")
for c in range(2,15,3) :
    print(c)

print("This is Case 5 where want to print number in reverse way")
for d in range(16,2,-1) :
    print(d)

print("This is Case 6 where we are using else block in for loop")
for j in range(14,2,-1) :
    print(j)
else:
    print("Inside Else Block")

print("End of the Program!!")