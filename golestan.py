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
class Golestan:
    def __init__(self,username,password,units):
        self.driver = webdriver.Chrome(
            path.join(path.dirname(__file__), 'chromedriver.exe'))
        self.driver.delete_all_cookies()
        self.waiter = WebDriverWait(self.driver, 10)
        self.username = username
        self.password = password
        self.units = units
        self.time = '9:00:00'

    def fillT01rows(self):
        print(self.toSeconds(self.time) - self.toSeconds(self.getSiteTime()))
        sleep(self.toSeconds(self.time) - self.toSeconds(self.getSiteTime()))
        self.driver.switch_to.default_content()
        self.waiter.until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/iframe')))
        self.waiter.until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
        self.waiter.until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
        counter = 0
        for i in self.units:
            script0 = 'window.frames[2].frames["Master"].frames["Form_Body"]'
            script1 = script0 + '.' + \
                'document.querySelectorAll("tr.inserted #F0780")[' + str(
                    counter)+'].value= "{}" '.format(str(i[:2]))
            script2 = script0 + '.' + \
                'document.querySelectorAll("tr.inserted #F0785")[' + str(
                    counter)+'].value= "{}"'.format(str(i[2:4]))
            script3 = script0 + '.' + \
                'document.querySelectorAll("tr.inserted #F0790")[' + str(
                    counter)+'].value="{}"'.format(str(i[4:7]))
            script4 = script0 + '.' + \
                'document.querySelectorAll("tr.inserted #F0795")[' + str(
                    counter)+'].value="{}" '.format(str(i[7:9]))

            self.driver.execute_script(script0 + '.AddRowT01()')
            self.driver.execute_script(script1)
            self.driver.execute_script(script2)
            self.driver.execute_script(script3)
            self.driver.execute_script(script4)
            counter += 1
        return self
    def setTime(self,time):
        self.time = time
    def login(self):
        self.driver.get(
            "https://golestan.sbu.ac.ir/Forms/AuthenticateUser/main.htm")
        inLogin = True
        while (inLogin):
            try:
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.ID, 'Faci1')))
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
                self.waiter.until(EC.element_to_be_clickable(
                    (By.ID, 'F80351'))).send_keys(self.username)
                self.driver.find_element_by_id('F80401').send_keys(self.password + Keys.ENTER)
                inLogin = False
            except TimeoutException:
                inLogin = True
        return self

    def goToPishkhaan(self):
        time = True
        while (time):
            try:
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.ID, 'Faci2')))
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
                self.waiter.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/table[1]/tbody/tr[3]/td[1]/table/tbody/tr/td[5]/nobr'))).click()
                time = False
            except TimeoutException:
                time = True
        return self

    def goToMainEntekhaabVahed(self):
        time = True
        while(time):
            try:
                self.driver.switch_to.default_content()
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.ID, 'Faci3')))
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Master')))
                self.waiter.until(
                    EC.frame_to_be_available_and_switch_to_it((By.NAME, 'Form_Body')))
                self.waiter.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'div #accordion2 label:nth-child(3)'))).click()
                self.waiter.until(EC.element_to_be_clickable(
                    (By.ID, 'L1'))).click()
                time = False
            except TimeoutException:
                time = True
        return self

    def getSiteTime(self):
        self.driver.switch_to.default_content()
        time = self.waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#\_mt_bou > div:nth-child(5)'))).text
        return time.split(' ')[0]
    def toSeconds(self,t):
        h = int(t.split(':')[0])
        m = int(t.split(':')[1])
        s = int(t.split(':')[2])
        return h *3600 + m *60 + s
