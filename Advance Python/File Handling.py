#Case 1 Write to a file
file = open("S:\\Python Projects\\FirstPythonProject\\Advance Python\\Sample.txt","w")         #Here w stands for writing and r stands for reading and a stands for appending
file.write("My Name is Sudhanshu Yadav.\n")
file.write("I am looking for Job of Automation QA.\n")
file.close()

#Case 2 Append a File
file = open("S:\\Python Projects\\FirstPythonProject\\Advance Python\\Sample.txt","a")         #Here w stands for writing and r stands for reading and a stands for appending
file.write("I am currently residing in Delhi and looking for a job in Delhi-NCR.")
file.close()

#Case 3 Read a File
file = open("S:\\Python Projects\\FirstPythonProject\\Advance Python\\Sample.txt","r")         #Here w stands for writing and r stands for reading and a stands for appending
#print(file.read())
#print(file.read(20))
lines = file.readlines()
for line in lines:
    print(line)
file.close()