def my_function():
    name = "Sudhanshu Yadav"            #This is a local variable
    print("My Name is : "+name)

my_function()
#print(name)           #This will Generate an Error Hence, commented out

Age = 25                #This is a Global Variable
def display_My_Age():
    print("Current Age is "+str(Age))

display_My_Age()
print("My age is : "+str(Age))      #Age Variable is accessible outside the function as it is a GLOBAL Variable

#Now let me show you another way of creating global variables
def show_my_lucky_number():
    global lucky_number         #Created A global variable by using global keyword
    lucky_number = 69
    print("My Number is : "+str(lucky_number))

show_my_lucky_number()
print("So, My Lucky Number is = "+str(lucky_number))

#Now what if Global & Local Variable have same name
#Let's discuss this issue too with upcoming code

city_Name = "New Delhi"                 #Here is a Global Variable
def show_My_City_Name():
    city_Name = "Delhi"                 #Here is a Local Variable
    print("I Live in the City of "+city_Name)

show_My_City_Name()
print("My Residence is in the City of "+city_Name)