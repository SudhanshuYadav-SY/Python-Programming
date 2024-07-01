#Case 1 Implement IN & NOT IN with List
colours_list = ['Red','Green','Blue']
print("Case 1 Output. . .")
print('Red' in colours_list)
print('Orange' in colours_list)
print('Blue' not in colours_list)
print('Yellow' not in colours_list)

#Case 2 Implement IN & NOT IN with Tuple
colours_tuple = ('Red','Green','Blue')
print("Case 2 Output. . .")
print('Red' in colours_tuple)
print('Orange' in colours_tuple)
print('Blue' not in colours_tuple)
print('Yellow' not in colours_tuple)

#Case 3 Implement IN & NOT IN with Sets
colours_set = {'Red','Green','Blue'}
print("Case 3 Output. . .")
print('Red' in colours_set)
print('Orange' in colours_set)
print('Blue' not in colours_set)
print('Yellow' not in colours_set)

#Case 4 Implement IN & NOT IN along with For loop with Range()
print("Case 4 Output. . .")
for i in range(len(colours_set)):       #Print Indexes
    print(i)

#Case 5 Implement IN & NOT IN along with For Each loop
print("Case 5 Output. . .")
for color in colours_set:               #Print Colours
    print(color)

#Case 6 Implement IN & NOT IN along with strings
a = ("Python is an Object Oriented Programming Language."
     "Python is very easy to understand and implement via Coding."
     "Python is Coded Using PyCharm IDE")
print("Case 6 Output. . .")
print('Python' in a)
print('JAVA' in a)
print('JAVA' not in a)
print('Pycharm IDE' not in a)