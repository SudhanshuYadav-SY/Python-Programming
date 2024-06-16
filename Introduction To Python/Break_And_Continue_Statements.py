print("This is an example of Break Statement in Python")
for i in range(1, 20):
    if i == 5 :
        break
    print(i)


print("This is an example of Continue Statement in Python")
for i in range(1, 20):
    if i == 5 :
        continue
    print(i)


print("This is an example of using While loop using Break Statement In Python")
i = 1
while i <= 10 :
    if i == 5:
        break
    print(i)
    i += 1

print("This is an example of using While loop using Continue Statement In Python")
i = 1
while i <= 10 :
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1