#Case 1 Basic Representation of a Tuple
print("Case 1 Output is here")
a = (12,5,8,7)
print(a)
#Case 2 Update Value of a element in a tuple
#a[1] = 9
#print(a)
#Case 3 find type of tuple
print("Case 3 Output is here")
print(type(a))
#Case 4 Indexing in a tuple
print("Case 4 Output is here")
print(a[2])                 #Forward Index
print(a[-2])                #Backward Index Because -2 + 4 = 2
#Case 5 Find length of a tuple
print("Case 5 Output is here")
print(len(a))
#Case 6 Using for loop in Tuple
print("Case 6 Output is here")
for i in range(len(a)):
    print(a[i])
print("Output of Case 6 Using For each loop is here")
for i in a:
    print(i)
#Case 7 Slicing up the Tuple
print("Case 7 Output is here")
print(a[1:3])
print(a[:3])
print(a[1:])
print(a[:])
#Case 8 Using IN And NOT IN Operator
