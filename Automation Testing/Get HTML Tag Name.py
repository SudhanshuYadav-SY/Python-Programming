import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")                       #Open Application URL

time.sleep(5)

HTML_Tag = driver.find_element(By.ID,"input-email").tag_name

time.sleep(5)

print("HTML Tag Name of the Field is - "+HTML_Tag)

driver.quit()