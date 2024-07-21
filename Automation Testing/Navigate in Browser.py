import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

time.sleep(5)

print("Title of the page currently is - "+driver.title)

driver.find_element(By.LINK_TEXT,"onlytestingblog").click()

time.sleep(5)

print("Title of the page currently is - "+driver.title)

driver.back()                                                       #Move Back to previous page in the Browser Window

print("Title of the page currently is - "+driver.title)


driver.quit()