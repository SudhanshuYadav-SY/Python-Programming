import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")

time.sleep(5)

links = driver.find_elements(By.TAG_NAME,"a")

time.sleep(3)

for link in links:
    print(link.get_attribute("href"))

driver.quit()