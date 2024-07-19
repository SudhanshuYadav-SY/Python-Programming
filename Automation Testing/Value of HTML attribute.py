import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

No_of_Columns = driver.find_element(By.ID,"ta1").get_attribute("cols")                       #Get Attribute Value

No_of_Rows = driver.find_element(By.ID,"ta1").get_attribute("rows")                         #Get Attribute Value of rows

print(No_of_Columns)                                                                              #Print Number of Columns attribute

print(No_of_Rows)                                                                                #Print Number of Rows Attribute

driver.quit()