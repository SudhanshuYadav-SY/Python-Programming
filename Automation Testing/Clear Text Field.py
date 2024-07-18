import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

#Let's first clear Text from text box

driver.find_element(By.ID,"textbox1").clear()                                               #Clear Pre-loaded text from text box

time.sleep(5)

#Now, Let's Clear Text from Text Area

driver.find_element(By.XPATH,"//*[text()='Text Area Field Two']/following::textarea").clear()       #Clear Pre-loaded Text from Text Area

time.sleep(5)

driver.quit()