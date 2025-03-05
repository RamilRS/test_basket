import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

answer = math.log(int(time.time()))

def test_basket(browser,language):
    link = "http://selenium1py.pythonanywhere.com/"+language+"/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements(By.CSS_SELECTOR,"button.btn-add-to-basket")
    assert button!=[]


