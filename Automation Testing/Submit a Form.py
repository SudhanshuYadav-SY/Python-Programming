import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")                       #Open Application URL

driver.find_element(By.NAME,"password").submit()

time.sleep(5)

driver.quit()