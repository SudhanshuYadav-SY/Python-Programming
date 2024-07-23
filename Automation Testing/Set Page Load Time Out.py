import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.set_page_load_timeout(10)

driver.get("https://tutorialsninja.com/demo/")                                                        #Open Application URL

#time.sleep(5)

driver.quit()