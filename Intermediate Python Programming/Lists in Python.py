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