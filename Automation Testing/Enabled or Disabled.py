import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

if driver.find_element(By.ID,"timerButton").is_enabled():                                           #Check Button is enabled or NOOT
    print("Button is Enabled")

else:
    print("Button is Disabled")