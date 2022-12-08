import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    time.sleep(5)
    x = time.time()
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    txt = browser.window_handles
    browser.switch_to.window(txt[1])


   
    num = browser.find_element(By.CSS_SELECTOR,'#input_value')
    z = calc(num.text)
    browser.find_element(By.CSS_SELECTOR, ' .form-control').send_keys(z)
    y = time.time()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(y-x)
