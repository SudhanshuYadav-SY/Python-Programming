import time

from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

driver.find_element(By.ID,"ta1").send_keys("Currently You are in maximise mode")

driver.fullscreen_window()                                                                      #View Web Page into Full Screen

time.sleep(5)

driver.find_element(By.ID,"ta1").clear()

time.sleep(4)

driver.find_element(By.ID,"ta1").send_keys("You are in Full Screen Now")

time.sleep(5)

driver.quit()