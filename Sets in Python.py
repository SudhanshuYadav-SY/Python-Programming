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