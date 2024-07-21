import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

driver.find_element(By.ID,"ta1").send_keys("Currently You are in Normal Size Mode")

time.sleep(5)

driver.find_element(By.ID,"ta1").clear()

time.sleep(5)

driver.set_window_size(1000,700)

driver.find_element(By.ID,"ta1").send_keys("Currently You are in user defined size mode")

time.sleep(5)