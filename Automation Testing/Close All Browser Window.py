import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

driver.find_element(By.LINK_TEXT,"Open a popup window").click()                             #Open a new Window

time.sleep(5)

driver.quit()                                                                                     #Close All Browsers in one go