import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

if driver.find_element(By.ID,"ta1").is_displayed():                                               #Checck if Text Area Field is displayed or not
    print("Yes Text Area Field Exists and Displayed on Web Page")                                  #if Above Statement is TRUE then print this

else:
    print("No Text Area Field Exists and Not Displayed On Web Page")                            #if Not Print this statement


time.sleep(5)

driver.get("https://tutorialsninja.com/demo/")

driver.find_element(By.XPATH,"//span[text()='My Account']").click()

driver.find_element(By.LINK_TEXT,"Login").click()

driver.find_element(By.NAME,"email").send_keys("amotooricap9@gmail.com")

driver.find_element(By.NAME,"password").send_keys("1234")

driver.find_element(By.XPATH,"//input[@class='btn btn-primary']").click()

time.sleep(5)

if driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed():
    print("User Login Successful")

else:
    print("User Unable to Login")

driver.quit()