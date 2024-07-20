import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

if driver.find_element(By.ID,"checkbox1").is_selected():                                        #Check Status of Radio Button
    print("Check box is Already Selected")

else:
    print("Check Box is NOT Selected")

print("\n\n\n\n")

if driver.find_element(By.ID,"checkbox2").is_selected():                                    #Check Status of Radio button
    print("Checkbox Button Selected")

else:
    print("Checkbox Button Not Selected")