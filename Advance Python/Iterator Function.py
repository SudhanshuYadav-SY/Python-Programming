a = [8,18,7,891]                            #Simple list

itr_A = iter(a)                               #Iterate Each And Every Item in a by creating an iterator "itr"


#Print each and every iterated element in a
print("Iterating Lists . . .")
print(next(itr_A))
print(next(itr_A))
print(next(itr_A))
print(next(itr_A))

b = (8,18,7,891)

itr_B = iter(b)                               #Iterate Each And Every Item in b by creating an iterator "itr"

#Print each and every iterated element in b

print("Iterating Tuple . . .")
print(next(itr_B))
print(next(itr_B))
print(next(itr_B))
print(next(itr_B))

c = {8,18,7,891}

itr_C = iter(c)                               #Iterate Each And Every Item in c by creating an iterator "itr"

#Print each and every iterated element in c

print("Iterating Sets . . .")
print(next(itr_C))
print(next(itr_C))
print(next(itr_C))
print(next(itr_C))