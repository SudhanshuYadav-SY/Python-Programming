Name = "Sudhanshu Yadav"
Experience = 2.6
Location = "New Delhi"
Subject = "Automation Testing"
Age = 23

print("My Name is : "+Name+" I Have Around ",str(Experience)+" in the field of "+Subject+" And I am Currently Living in "+Location)
print("My Name is : "+Name+" I Have Around",Experience," in the field of "+Subject+" And I am Currently Living in "+Location)
print("My Name is : {}. I have Around {} years of experience in {} And I am Currently Living in {}".format(Name,Experience,Subject,Location))
print("My Name is : {}. I have Around {} years of experience in {} And I am Currently Living in {}".format(Experience,Subject,Location,Name))
print("My Name is : {3}. I have Around {0} years of experience in {2} And I am Currently Living in {1}".format(Experience,Location,Subject,Name))
print("My Name is : %s,I am %d years old I have Around %g years of experience in %s And I am Currently Living in %s"%(Name,Age,Experience,Subject,Location))