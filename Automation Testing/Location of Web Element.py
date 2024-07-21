import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                        #Open Application URL

time.sleep(5)

WebElement_location = driver.find_element(By.ID,"ta1").location                                     #Find co-ordinates of web element

print(WebElement_location)

print("\n\n")

print("X Co-Ordinate of Web Element is - "+str(WebElement_location.get("x")))

print("Y Co-Ordinate of Web Element is - "+str(WebElement_location.get("y")))

driver.quit()