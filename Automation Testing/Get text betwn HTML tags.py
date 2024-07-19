import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

text = driver.find_element(By.ID,"pah").text                                                 #Get Text from Web Element

button = driver.find_element(By.ID,"button9").text                                           #Get Text from Web Element

text_Area_Text = driver.find_element(By.XPATH,"//*[text()='Text Area Field Two']/following::textarea").text         #Get Text from Web element

time.sleep(4)

print("Actual Text is : \n"+text)                                                                                       #Print that Text got

print("Button label is : \n"+button)                                                                                     #Print that Text

print("Pre-exist Text in Text Area : \n"+text_Area_Text)

driver.quit()