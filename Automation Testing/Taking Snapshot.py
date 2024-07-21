import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")                       #Open Application URL

time.sleep(5)

driver.find_element(By.NAME,"email").send_keys("amotooricap9@gmail.com")

driver.find_element(By.NAME,"password").send_keys("12345")

driver.find_element(By.NAME,"password").submit()

time.sleep(5)

driver.save_screenshot("login.jpg")

driver.get_screenshot_as_file("login.jpg")

driver.quit()