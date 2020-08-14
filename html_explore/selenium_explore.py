import selenium
from selenium import webdriver
import chromedriver_binary

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://canvas.case.edu')