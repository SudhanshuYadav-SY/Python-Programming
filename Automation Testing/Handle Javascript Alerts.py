import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://the-internet.herokuapp.com/")                                                 #Open Application URL

driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()

time.sleep(5)

driver.find_element(By.XPATH,"//*[text()='Click for JS Prompt']").click()

time.sleep(5)

#This code will generate error as we did not handle previous exception
"""driver.find_element(By.XPATH,"//*[text()='Click for JS Confirm']").click()

time.sleep(5)
"""
#Now lets handle this alert which pooped out

info_alert = driver.switch_to.alert

print("Alert Text is -\n"+info_alert.text)

info_alert.send_keys("Hello I am Sudhanshu Yadav")

info_alert.accept()

print("Result is -\n"+driver.find_element(By.ID,"result").text)

time.sleep(5)

driver.quit()