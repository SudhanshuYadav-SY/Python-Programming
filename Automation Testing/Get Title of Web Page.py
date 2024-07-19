import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://omayo.blogspot.com/")                                                         #Open Application URL

title_1 = driver.title                                                                               #Get Title of Web Page

time.sleep(5)

print("You first visited the site of : \n"+title_1)                                                #Print Title of Web Page

driver.find_element(By.LINK_TEXT,"onlytestingblog").click()                                    #Navigate to a new web page

title_2 = driver.title

time.sleep(5)

print("You are Currently on : \n"+title_2)                                                                                     #Print Title of Web page 2

driver.quit()                                                                                      #Quit automation browser