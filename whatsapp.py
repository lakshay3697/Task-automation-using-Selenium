from selenium import webdriver

try:
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
except:
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

driver.get('https://web.whatsapp.com/')

name = raw_input('Enter the name of user or group you want to send messages to :-')
count = int(raw_input('Enter the count of messages :-'))

#input('Enter anything after QR code has scanned properly to proceed')

user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

msg="."

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    msg=msg+"."