import re

pattern = "S.......u"                              #Check if certain text is present in the text
print("Enter Sample Text")
text = input()
if re.search(pattern,text):

    print("Pattern Matched Successfully")

else:

    print("Pattern Not Matched")