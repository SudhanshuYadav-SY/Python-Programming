
from selenium import webdriver

driver = webdriver.Chrome()                                                 #Launch Chrome Browser
driver.maximize_window()                                                    #This Will Maximise Automation Window
driver.get("https://www.google.com/")                                       #Open First Application URL
driver.get("https://tutorialsninja.com/demo/")                              #Opem Another Application URL