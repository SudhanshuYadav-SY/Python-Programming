import time

from selenium import webdriver

driver = webdriver.Chrome()                                                 #Launch Chrome Browser
driver.maximize_window()                                                    #This Will Maximise Automation Window
driver.get("https://www.google.com/")                                       #Open First Application URL
driver.get("https://tutorialsninja.com/demo/")                              #Opem Another Application URL
time.sleep(5)                                                               #Sleep for 5 seconds
driver.minimize_window()                                                    #This will Minimise Application Window