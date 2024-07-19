import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

url_1 = driver.current_url

print("\n\n")

print("Current URL is - "+url_1)

time.sleep(5)

driver.find_element(By.LINK_TEXT,"onlytestingblog").click()

url_2 = driver.current_url

time.sleep(5)

print("\n\n")

print("Now the URL is - "+url_2)

driver.quit()