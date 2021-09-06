from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)

title_data = ["abcd1234", "teszt233@", "abcd"]
result_data = ["", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]

input_title = driver.find_element_by_id("title")

""" TC01 - Helyes kitöltés esete:
o	title: abcd1234
o	Nincs validációs hibazüzenet"""


def test_good_data():
    input_title.send_keys(title_data[0])
    error = driver.find_element_by_xpath('//span[@class="error"]')
    assert error.is_displayed() == False


""" TC02 - Illegális karakterek esete:
o	title: teszt233@
o	Only a-z and 0-9 characters allewed."""


def test_illegal_char():
    input_title.clear()
    input_title.send_keys(title_data[1])
    error_active = driver.find_element_by_xpath('//span[@class="error active"]')
    assert error_active.text == result_data[1]


""" TC03 - Tul rövid bemenet esete:
o	title: abcd
o	Title should be at least 8 characters; you entered 4."""


def test_short_input():
    input_title.clear()
    input_title.send_keys(title_data[2])
    assert error_active.text == result_data[2]

    driver.close()
