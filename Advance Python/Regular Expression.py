import re

pattern = "[Pp]ython"               #Check if text starts with P or p then is the pattern and text matching or not
print("Enter Sample Text")
text = input()
if re.search(pattern,text):

    print("Pattern Matched Successfully")

else:

    print("Pattern Not Matched")