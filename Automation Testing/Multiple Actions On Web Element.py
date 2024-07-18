import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL
"""
driver.find_element(By.NAME,"fname").click()                                                #Navigate to Text Box

time.sleep(5)

driver.find_element(By.NAME,"fname").clear()                                                #Clear That Text Field

time.sleep(2)

driver.find_element(By.NAME,"fname").send_keys("Sudhanshu Yadav")                           #Type Some Text in Text Field

time.sleep(2)

driver.find_element(By.NAME,"fname").clear()                                                #Clear That Text Field

time.sleep(2)

driver.find_element(By.NAME,"fname").send_keys("Selenium Python")                           #Type Some Text in Text Field

time.sleep(2)

driver.find_element(By.NAME,"fname").clear()                                                #Clear That Text Field

time.sleep(2)

driver.quit()                                                                                     #Close Automation Window
"""

#Alternatively we can do one thing in-place of so many driver.find_element
#We can optimise our code as shown below:

text_field = driver.find_element(By.NAME,"fname")                                  #Store Web Element as a variable

text_field.click()                                                                      #Navigate to Web-Element

time.sleep(5)

text_field.clear()                                                                      #Clear that Text Field

time.sleep(5)

text_field.send_keys("Sudhanshu Yadav")                                                 #Enter Text in Text Field

time.sleep(5)

text_field.clear()                                                                      #Clear that Text Field

time.sleep(5)

text_field.send_keys("Selenium Python")                                                 #Enter Text in Text Field

time.sleep(5)

text_field.clear()                                                                      #Clear that Text field

time.sleep(5)