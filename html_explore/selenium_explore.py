from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Using Chrome to access web
driver = webdriver.Chrome(ChromeDriverManager().install())
# Open the website
driver.get('https://canvas.case.edu')