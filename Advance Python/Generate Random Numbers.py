import random

print(random.random())                                  #Any random floating point value will be printed between 0 & 1
print(random.random()*100)                              #Any random floating point value will be printed between 0 & 100
print(int(random.random()*100))                         #Any random int value will be printed between 1 & 100

print(random.randint(1,20))                       #Print any random int value from 1 to 20 with both 1 and 20 included
print(random.randint(1,100))                      #Print any random int value from 1 to 20 with both 1 and 100 included

