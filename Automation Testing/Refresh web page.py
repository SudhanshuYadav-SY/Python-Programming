import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

print("Before Refreshing, Title of the page currently is - "+driver.title)

driver.refresh()                                                                                #Refresh the Web page

print("After Refreshing, Title of the page currently is - "+driver.title)

driver.quit()