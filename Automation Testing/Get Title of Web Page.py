import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

title = driver.title                                                                               #Get Title of Web Page

print("You recently visited the site of : \n"+title)                                                           #Print Title of Web Page

driver.quit()                                                                                      #Quit automation browser