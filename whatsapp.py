#!/usr/local/env python2 

from selenium import webdriver

import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

class WhatsApp(object):
    def __init__(self):
        self.search_bar_css = ".cBxw- > ._3FRCZ"
        self.text_box_css = "._2FVVk._2UL8j > ._3FRCZ"
        self.url = "https://web.whatsapp.com/"
        self.driver = None

    def start_session(self):
        options = Options()
        options.add_argument("--user-data-dir=session")
        driver = webdriver.Chrome(
                executable_path='/Users/ccb/Downloads/chromedriver',
                options=options
                )
        driver.get('https://web.whatsapp.com/')
        self.driver = driver
        return driver

    def send_message(self, message, recipient):
        self.send_element(recipient, self.search_bar_css)
        self.send_element(message, self.text_box_css)

    def get_message_status(self, recipient):
        self.send_element(recipient, self.search_bar_css)
        ticks = self.driver.find_element_by_css_selector("div._1qPwk")
        ticks_html = ticks.get_attribute("innerHTML")
        status = ticks_html.split(' ')[3]
        return str(status) 

    def send_element(self, message, css_selector):
        self.wait_to_load(20)
        search = self.driver.find_element_by_css_selector(css_selector)
        search.send_keys(message+Keys.ENTER)

    def wait_to_load(self, wait_time):
        WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '._3FRCZ')))

    def quit_on_message_status(self, recipient):
        message_status = self.get_message_status(recipient)
        start = time.time()
        while message_status == 'Pending' and (time.time() - start) < 30:
            time.sleep(1) 
        self.driver.quit()

def message_randomiser(message_list):
    max_index = len(message_list) - 1
    index = randint(0, max_index)
    msg = message_list[index]
    return msg


if __name__=="__main__":
    message_list = [line.strip('\n') for line in open('messages.txt', 'r')]
    msg = message_randomiser(message_list)

    wa = WhatsApp()
    wa.start_session()
    recipient = 'Christie'
    wa.send_message(msg, recipient)
    wa.quit_on_message_status(recipient)
