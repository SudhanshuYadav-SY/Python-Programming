import re

pattern = "S.......u"                              #Check if not of 0 to 9 is there in text pattern that is pattern should not start with number
print("Enter Sample Text")
text = input()
if re.search(pattern,text):

    print("Pattern Matched Successfully")

else:

    print("Pattern Not Matched")