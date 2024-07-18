import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser
driver.maximize_window()                                                                          #This Will Maximise Automation Window
driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL
driver.find_element(By.ID,"ta1").send_keys("My Name is Sudhanshu \n\n\n\n\n And Currently Learning Python")     #Interact with Web Element
time.sleep(5)
driver.quit()