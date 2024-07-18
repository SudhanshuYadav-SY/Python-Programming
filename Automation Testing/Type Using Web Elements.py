import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser
driver.maximize_window()                                                                          #This Will Maximise Automation Window
driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL
driver.find_element(By.ID,"ta1").send_keys("My Name is Sudhanshu \n\n\n\n\nAnd Currently Learning Python")     #Type Text in Text Area
time.sleep(5)
driver.find_element(By.NAME,"q").send_keys("Automation Testing")                #Type Text in Text Box
time.sleep(5)
driver.find_element(By.NAME,"pswrd").send_keys("Shob@1234")                     #Type Password Text in Text Box
time.sleep(5)
driver.quit()