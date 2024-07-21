import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                        #Open Application URL

time.sleep(5)

WebElement_Size = driver.find_element(By.ID,"ta1").size

print(WebElement_Size)

print("Height of the Field is - "+str(WebElement_Size.get("height")))

print("Width of the Field is - "+str(WebElement_Size.get("width")))

driver.quit()