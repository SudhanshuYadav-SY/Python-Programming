#Case 1 Basic Representation of a Tuple
print("Case 1 Output is here")
a = (12,5,8,7,12,54,12)
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
print("Case 8 Output is here")
print(5 in a)
print(5 not in a)
print(77 in a)
print(77 not in a)
#Case 9 Use Count() in a tuple
print("Case 9 Output is here")
print(a.count(12))          #Count Occurrence of that number in the tuple
print(sum(a))               #Print sum of all elements in the tuple
print(max(a))               #Print maximum in the tuple
print(min(a))               #Print minimum in the tuple
print(a.index(5))           #Print the index where that element is present
b = (4,7,2,1)
print(b)
#del b
#print(b)
#Nested Tuple
c = (4,(4,8,10,1),2,1)
print(c)
print(c[1][3])
d = (4,[4,8,10,1],2,1)      #List inside a tuple
d[1][3] = 19
print(d)

#Case 10 Type Casting a String to Tuple
print("Case 10 Output is here")
name = tuple("Sudhanshu")
print(name[6])
for h in name:
    print(h)