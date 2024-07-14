print("Case 1 . . .")
a = range(3)                                #Basic demonstration of numbers from 0 to 3
print(a)                                    #Print Range from 0 to 3
print(type(a))                              #Print data-type of the variable a

print("Case 2 . . .")
for v in a:                                 #For each value in the range print that variable v
    print(v)

b = range(2,10)                             #This will show numbers from 1 and end at 9
print("Case 3 . . .")
for c in b:
    print(c)

d = range(-2,10,3)                              #Here numbers from 2 to 10 with a gap of 3 will be printed
print("Case 4 . . .")
for e in d:
    print(e)


f = range(12,-2,-3)                             #Reverse Range from 12 to -2 but will end at 0 in console
print("Case 5 . . .")
for g in f:
    print(g)

h = range(6,15,3)                              #Print Numbers from 6 to 15 with increment of 3 at each step
print("Case 6 . . .")
print(h[0])                                   #Print 0th Element in the range
print(h[1])                                   #Print 1st Element in the range
print(h[2])                                   #Print 2nd Element in the range