# source code: https://github.com/samarth1011/Whatsapp_Automation_Selenium/blob/main/whatsapp.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver=webdriver.Chrome(r'C:\Users\Jean-Pierre\.wdm\drivers\chromedriver\win32\91.0.4472.101\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name = '+41 76 822 49 87'
filepath = "D:\\Users\\Jean-Pierre\\Downloads\\snap13.jpg"
input('Scan QR code and then type RETURN')
print('Now sending {} to {} ...'.format(filepath, name))
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

message_text = driver.find_element_by_class_name('_13NKt')
message_text.send_keys('Coucou')
message_text.click()
attachment_box = driver.find_element_by_xpath('//div[@title="Joindre"]')
attachment_box.click()
image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)
addfile_button = driver.find_element_by_xpath('//input[@accept="*"]')
sleep(4)
send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()
sleep(1)
