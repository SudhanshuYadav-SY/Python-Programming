import time
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                                                                       #Launch Chrome Browser

driver.maximize_window()                                                                          #This Will Maximise Automation Window

driver.get("https://the-internet.herokuapp.com/basic_web_page.htnl")                                                         #Open Application URL

time.sleep(5)

HTML_Code = driver.page_source                                                                  #Command to get HTML Source Code

soup = BeautifulSoup(HTML_Code,'html.parser')                                           #Use Beautiful Soup to Parse the HTML Code

pretty_html = soup.prettify()                                                                   #Format the respective HTML Code in a pretty way

print("Non- Pretty HTML Code for the page - \n"+HTML_Code)                                      #Print Non-Pretty HTML Code

print("Pretty HTML Code for the page is - \n"+pretty_html)                                      #Print the Pretty HTML Code