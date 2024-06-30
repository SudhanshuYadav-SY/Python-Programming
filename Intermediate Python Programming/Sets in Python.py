#Case 1 Default Implementation of Set
print("Output of Case 1 is here")
a = {2,7,9,1,0}
print(a)
#Case 2 Print Set With Index
#print(a[1])
#Case 3 Check Duplicate Elements
d = {1,8,1,7,1,5}
print("Output of Case 3 is here")
print(d)
#Case 4 Print Type of Set
print("Output of Case 4 is here")
print(type(d))
#Case 5 Print Size of Set
print("Output of Case 5 is here")
print(len(d))
#Case 6 Add Elements to the Set
print("Output of Case 6 is here")
print(a)
a.add(5)
a.add(13)
print(a)
#Case 7 Using Update()
print("Output of Case 7 is here")
print(a)
a.update([16,7,91])
print(a)
#Case 8 Removing the values from Set
print("Output of Case 8 is here")
print(a)
a.remove(5)
print(a)
#a.remove(15)                #Removing element which is not present in SET
#print(a)
#Case 9 Using Discard()
print("Output of Case 9 is here")
a.discard(15)
print(a)
#Case 10 Using Pop() in sets
print("Output of Case 10 is here")
print(a)
a.pop()
print(a)
a.pop()
print(a)
#Case 11 Removing all elements in one go using clear()
print("Output of Case 11 is here")
print(d)
d.clear()
print(d)
#Case 12 Delete Entire Set
print("Output of Case 12 is here")
print(d)
#del d
#print(d)
#Case 13 For Each loop in Set
print("Output of Case 13 is here")
for e in a:
    print(e)
#Case 14 Use of IN and NOT IN Operator
print("Output of Case 14 is here")
print(7 in a)
print(5 in a)
print(13 not in a)
print(13 in a)
#Case 15 Nested Sets or Lists are not possible in SETs But Tuples are allowed
print("Output of Case 15 is here")
d = {1,7,(5,4,0),6}
print(d)
#Case 16 Convert List to set
print("Output of Case 16 is here")
# Example list
b = [1, 2, 2, 3, 4, 4, 5]
print(type(b))
s = set(b)                      # Typecasting list to set
print(type(s))                  # Printing the type of the set
#Case 17 Using Union() Operator
print("Output of Case 17 is Here")
c = {6,8,9,0}
d = {5,0,4,1}
print(c.union(d))           #Alternatively you can use OR Here
print(c.__or__(d))         #Also you can use | here
#Case 18 Using Intersection() Operator
print("Output of Case 18 is Here")
print(c.intersection(d))
#Case 19 Using Difference() Operator
print("Output of Case 19 is Here")
print(c - d)
print(d - c)
#Case 20 Using Symmetric Difference that is common will be removed other values will be printed
print("Output of Case 20 is Here")
print(c.symmetric_difference(d))
print(c ^ d)
#Case 21 Using Max & Min in set
print("Output of Case 21 is Here")
print(max(c))
print(min(d))
print(sum(a))