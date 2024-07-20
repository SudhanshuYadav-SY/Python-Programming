import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

if driver.find_element(By.ID,"hbutton").is_displayed()   :                                        #If Button is visible or not
    print("Hidden Button is There")

else:
    print("Hidden Button is NOT Displayed")

driver.quit()