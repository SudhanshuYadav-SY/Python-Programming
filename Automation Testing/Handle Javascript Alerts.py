import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://the-internet.herokuapp.com/")                                                 #Open Application URL

driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()

time.sleep(5)

driver.find_element(By.XPATH,"//*[text()='Click for JS Alert']").click()

time.sleep(5)

driver.find_element(By.XPATH,"//*[text()='Click for JS Confirm']").click()

time.sleep(5)

driver.quit()