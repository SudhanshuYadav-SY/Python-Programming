#Case 1 : General Implementation of Lists in Python

a = [9,1,8,5]                           #Indexing
print("Output for Case 1 are Below . . .")
print(a)                                #Print Entire List
print(a[2])                             #Printing Specific Element in Lists
b = str(len(a))                         #Calculating length of list
print("Length of List A = "+b)          #Printing Length of List

#Case 2 : Implementation of Lists in For Loop

c = [12,5,6,8,1,]
print("Output for Case 2 are Below . . .")
for i in range(len(c)):
    print(i)
    print(c[i])


#Case 3 Using Lists in For-Each loop
j = [17,8,51,9,81,45]
print("Output for Case 3 Are Below . . .")
for t in j:
    print(t)

#Case 4 Updating values of elements in the list
k = [45,25,8,19]
print("Output for Case 4 are Below . . .")
print(k)
k[2] = 56
print(k)

#Case 5 Append element at the end of list

h = [3,17,9,12,7]
print("Output for Case 5 Are Below . . .")
print(h)
h.append(6)
print(h)

#Case 6 Inserting a element at a particular position
g = [19,78,45,18,90]
print("Output for Case 6 Are Below . . .")
print(g)
g.insert(2,20)
print(g)

#Case 7 Remove elements from list
g.remove(20)
print("Output as per Case 7 is Below . . .")
print(g)

#Case 8 Removing last element from list
g.pop()
print("Output as per Case 8 is Below . . .")
print(g)

#Case 9 Remove all elements using Clear()
print("Output as per Case 9 is Below . . .")
print(k)
k.clear()
print(k)

#Case 10 Print the pop element
print("Output as per Case 10 Are Below . . .")
print(c)
print(c.pop(1))
print(c)

#Case 11 Reverse all elements in the list
print("Output as per Case 11 Are Below . . .")
print(j)
j.reverse()
print(j)

#Case 12 Sort out all elements in the list
print("Output as per Case 12 Are Below . . .")
print(a)
a.sort()
print(a)
""""
colors = ["Red","Yellow","Green","Black"]
colors.sort()
print(colors)"""

#Case 13 Access Elements on the basis of Index
print("Output as per Case 13 Are Below . . .")
print(a)
print(a.index(5))

#Case 14 Nested List
print("Output as per Case 14 Are Below . . .")
A = [12,[6,4,98,12],8,19]
print(A[1])
print(A[1][3])

#Case 15 Storing Different Data Types in list
H = ["Honda","Swift",14.5,"True"]
print("Output as per Case 15 Are Below . . .")
print(H[0])
print(H[1])
print(H[2])

#Case 16 Print Elements with Negative Indexes
print("Output as per Case 16 Are Below . . .")
print(H[2])
print(H[-2])                        #It's OK Because -2 + 4 = 2 so element at index 2 will be printed

#Case 17 Slicing up lists
print("Output as per Case 17 Are Below . . .")
print(a)
print(a[1:3])               #index : position
print(a[1:])                #index : last position
print(a[:])                 #first index : last position

#Case 18 : Count repetition of a number in a list
print("Output as per Case 18 Are Below . . .")
l = [1,14,1,788,12,1,17,1,89]
print(l.count(1))

#Case 19 Find max and min in a list
print("Output as per Case 19 Are Below . . .")
print(max(l))
print(min(l))

#Case 20 Add Sum of elements in list
print("Output as per Case 20 Are Below . . .")
print(sum(l))

#Case 21 Identify Data Types in list
print("Output as per Case 21 Are Below . . .")
print(type(l))

#Case 22 Delete A List
#print("Output as per Case 22 Are Below . . .")
#print(H)
#del H
#print(H)

#Case 23 Check if element exists or not
print("Output as per Case 23 Are Below . . .")
print(5 in a)
print(23 in a)

#Case 24 Concate 2 lists
print("Output as per Case 24 Are Below . . .")
print(a)
print(c)
S = a + c
print(S)

#Case