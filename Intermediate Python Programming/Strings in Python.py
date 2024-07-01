first_name = "Sudhanshu"
last_name = 'Yadav'
location = str("Delhi")
#Case 1 Print values of strings
print("Case 1 Output . . .")
print(first_name)
print(last_name)
print(location)
#Case 2 Print data type of Variables
print("Case 2 Output . . .")
print(type(first_name))
print(type(last_name))
print(type(location))
#Case 3 String works like Collection
print("Case 3 Output . . .")
print(first_name[0])
for c in first_name:
    print(c)
#Case 4 Find length of string
print("Case 4 Output . . .")
print(len(first_name))
for i in range(len(first_name)):
    print(first_name[i])
#Case 5 Use of in & Not in String
print("Case 5 Output . . .")
print("Sud" in first_name)
print("Sud" not in first_name)
print("Yad" not in last_name)
print("Yad " in last_name)
#Case 6 Slicing Strings
print("Case 6 Output . . .")
print(first_name[1:5])
print(first_name[:5])
print(first_name[1:])
#Case 7 Modify Strings
print("Case 7 Output . . .")
n = "     Sud Yadav   "
print(first_name.upper())
print(first_name.lower())
print(n.strip())