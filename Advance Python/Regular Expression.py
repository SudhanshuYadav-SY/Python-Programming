import re

pattern = "[abcdefghijklmnopqrstuvwxyz]it"                              #Check if text starts with a certain pattern then is the pattern and text matching or not
print("Enter Sample Text")
text = input()
if re.search(pattern,text):

    print("Pattern Matched Successfully")

else:

    print("Pattern Not Matched")