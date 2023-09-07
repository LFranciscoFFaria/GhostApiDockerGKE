# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Postv2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_postv2(self):
        driver = self.driver
        driver.get("http://{{ ghost_ip }}:80/ghost/#/signin")
        driver.find_element("xpath","//input[@placeholder = \"jamie@example.com\"]").click()
        driver.find_element("xpath","//input[@placeholder = \"jamie@example.com\"]").clear()
        driver.find_element("xpath","//input[@placeholder = \"jamie@example.com\"]").send_keys("ascn@example.com")
        driver.find_element("xpath","//input[@placeholder = \"•••••••••••••••\"]").click()
        driver.find_element("xpath","//input[@placeholder = \"•••••••••••••••\"]").clear()
        driver.find_element("xpath","//input[@placeholder = \"•••••••••••••••\"]").send_keys("ascn123")
        driver.find_element("xpath",u"//*[text() = \"Sign in →\"]").click()
        driver.find_element(By.CSS_SELECTOR,"#ember21 > span > svg").click()
        driver.find_element("xpath","//textarea[@placeholder = \"Post title\"]").click()
        driver.find_element("xpath","//textarea[@placeholder = \"Post title\"]").clear()
        driver.find_element("xpath","//textarea[@placeholder = \"Post title\"]").send_keys("O alex é lindo!\n")
        driver.find_element("xpath","//*[text() = \"Publish\"]").click()
        driver.find_element("xpath",u"//*[text() = \"Continue, final review →\"]").click()
        driver.find_element("xpath","//*[text() = \"Publish post, right now\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()