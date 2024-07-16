import re

pattern = "Sudhanshu"
print("Enter Sample Text")
text = input()
if re.search(pattern,text):

    print("Pattern Matched Successfully")

else:

    print("Pattern Not Matched")