import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

if driver.find_element(By.ID,"ta1").is_displayed():                                                   #Checck if Text Area Field is displayed or not
    print("Yes Text Area Field Exists and Displayed on Web Page")

else:
    print("No Text Area Field Exists and Not Displayed On Web Page")


time.sleep(5)

driver.quit()