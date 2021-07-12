from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
name = '+41 76 822 49 87'
filepath = "D:\\Users\\Jean-Pierre\\Downloads\\download.jpg"

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
#input('wait')
attachment_box=driver.find_element_by_xpath('//div[@title="Joindre"]')
attachment_box.click()
image_box=driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)
addfile_button=driver.find_element_by_xpath('//input[@accept="*"]')
addfile_button.send_keys(filepath)
sleep(1)
sleep(4)
send_button=driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()
sleep(1)
