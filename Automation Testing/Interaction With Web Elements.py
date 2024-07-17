import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                 #Launch Chrome Browser
driver.maximize_window()                                                                    #This Will Maximise Automation Window
driver.get("https://omayo.blogspot.com/")                                                   #Open Application URL
driver.find_element(By.ID,"ta1").send_keys("Hello My Name is Sudhanshu")               #Type Text in that Field as we identify Web Element using ID
time.sleep(4)                                                                                #Wait for 4 seconds on web page
driver.quit()                                                                                #Close Automation Window
