import datetime

D = datetime.datetime(2024,7,16,12,33,40)               #Initialize Date and time and store in a variable

print("Current Date And Time = "+str(D))                                                                                 #Print Date And Time
print("Where . . .")
print("Date = "+str(D.date()))                                  #Print Only Date
print("Time = "+str(D.time()))                                  #Print Only Time
print("Year = "+str(D.year))                                    #Print Only Year
print("Month = "+str(D.month))                                  #Print Only Month
print("Date = "+str(D.day))                                     #Print Only Day
print("Hour = "+str(D.hour))                                    #Print Only Hour
print("Minutes = "+str(D.minute))                               #Print Only Minute
print("Seconds = "+str(D.second))                               #Print Only Seconds

print("Now let's Print Statements in String Format Time")

print(D.strftime("%dth %B, %Y"))