import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

text = driver.find_element(By.ID,"pah").text                                                  #Get Text from Web Page

time.sleep(4)

print(text)                                                                                       #Print that Text got

driver.quit()