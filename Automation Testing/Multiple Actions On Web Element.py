import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

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