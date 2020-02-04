from selenium import webdriver
from os import path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import events
from time import sleep
from selenium.common.exceptions import TimeoutException
#enter unit ids that you want to take first
v = ['350101702', '350105003']
username = '__replace-with-your-username__'
password = '__replace-with-your-password__'

inLogin = True
driver = webdriver.Chrome(
    path.join(path.dirname(__file__), 'chromedriver.exe'))
driver.delete_all_cookies()
waiter = WebDriverWait(driver, 10)
driver.get("https://golestan.sbu.ac.ir/Forms/AuthenticateUser/main.htm")
while (inLogin):
    try:
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'Faci1')))
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'F80351'))).send_keys(username)
        driver.find_element_by_id('F80401').send_keys(password + Keys.ENTER)
        inLogin = False
    except TimeoutException as e:
        inLogin = True
time = True
sleep(7)
while (time):
    try:
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'Faci2')))
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table[1]/tbody/tr[3]/td[1]/table/tbody/tr/td[5]/nobr'))).click()
        time = False
    except TimeoutException:
        time = True

time = True

while(time):
    try:
        driver.switch_to.default_content()
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, 'Faci3')))
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div #accordion2 label:nth-child(3)'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.ID, 'L1'))).click()
        time = False
    except TimeoutException:
        time = True
driver.switch_to.default_content()
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/iframe')))
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
sleep(5)
counter = 0
for i in v:
    script0 = 'window.frames[2].frames["Master"].frames["Form_Body"]'
    script1 = script0+ '.' + 'document.querySelectorAll("tr.inserted #F0780")[' +str(counter)+'].value= "{}" '.format(str(i[:2]))
    script2 = script0+ '.' + 'document.querySelectorAll("tr.inserted #F0785")[' +str(counter)+'].value= "{}"'.format(str(i[2:4]))
    script3 = script0+ '.' + 'document.querySelectorAll("tr.inserted #F0790")[' +str(counter)+'].value="{}"'.format(str(i[4:7]))
    script4 = script0+ '.' + 'document.querySelectorAll("tr.inserted #F0795")[' +str(counter)+'].value="{}" '.format(str(i[7:9]))

    driver.execute_script(script0 + '.AddRowT01()')
    driver.execute_script(script1)
    driver.execute_script(script2)
    driver.execute_script(script3)
    driver.execute_script(script4)
    counter += 1

print ('every thing is ok')
