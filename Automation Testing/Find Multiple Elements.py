import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")

options = driver.find_elements(By.XPATH,"//select[@id='multiselect1']/option")

print("You only have "+str(len(options))+" Cars to choose from")

print("Your Options are - ")

for i in options:
    print(i.text)

driver.quit()