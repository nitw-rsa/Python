'''
Auhtor: Rishabh Sharma
'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

WINDOW_SIZE = "1920,2080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--log-level=3')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(chrome_options=chrome_options)

cr_no_url = "https://facebook.com"
browser.get(cr_no_url)

ctrd = browser.find_element_by_id(id1)
val = ctrd.get_attribute("value")
ctrd.click()
ctrd.send_keys(Keys.CONTROL + "a")
ctrd.send_keys(Keys.DELETE)
ctrd.send_keys(new_value)

select_element = browser.find_element_by_xpath("//select[option[@value = '%s']]" % option_value)
select = Select(select_element)
select.select_by_value(option_value)

browser.execute_script("window.scrollTo(0, 1080);")
time.sleep(5)

select_element = browser.find_element_by_xpath("//select[option[@value = '%s']]" % option_value)
select = Select(select_element)
select.select_by_value(option_value)

collapsible_element_id_elem1 = browser.find_element_by_class_name("collapsible-element")
collapsible_element_id_elem1.click()
time.sleep(8)
