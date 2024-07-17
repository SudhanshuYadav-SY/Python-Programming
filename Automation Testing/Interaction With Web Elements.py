import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                 #Launch Chrome Browser
driver.maximize_window()                                                                    #This Will Maximise Automation Window
driver.get("https://omayo.blogspot.com/")                                                   #Open Application URL
driver.find_element(By.ID,"ta1").send_keys("Hello My Name is Sudhanshu")               #Identify Web Element using ID
driver.find_element(By.NAME,"q").send_keys("Automation Testing")                       #Identify Web Element using NAME
driver.find_element(By.CLASS_NAME,"dropbtn").click()                                   #Identify Web Element using CLASS NAME
driver.find_element(By.LINK_TEXT,"compendiumdev").click()                              #Identify Web Element Using LINK TEXT
time.sleep(4)                                                                                #Wait for 4 seconds on web page
driver.quit()                                                                                #Close Automation Window