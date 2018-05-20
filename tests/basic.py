# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

if __name__ == '__main__':
    browser = os.environ.get('BROWSER', 'CHROME')
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
    )
    driver.get("https://ok.ru/")
    driver.quit()
