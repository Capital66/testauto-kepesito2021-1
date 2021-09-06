from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)

a_test_data = ["", "2", ""]
b_test_data = ["", "3", ""]
c_result_data = ["", "10", "NaN"]

a_input = driver.find_element_by_id("a")
b_input = driver.find_element_by_id("b")
submit_button = driver.find_element_by_id("submit")
results = driver.find_element_by_id("results")
result = driver.find_element_by_id("result")

""" TC01 - Helyesen jelenik meg az applikáció betöltéskor:
	a: <üres>
	b: <üres>
	c: <nem látszik>"""

def test_good_app():
    a_input.send_keys(a_test_data [0])
    b_input.send_keys(b_test_data [0])
    assert results.text == "display: none;"

""" TC02 - Számítás helyes, megfelelő bemenettel
	a: 2
	b: 3
	c: 10"""

def test_good_data():
    a_input.send_keys(a_test_data [1])
    b_input.send_keys(b_test_data [1])
    submit_button.click()
    assert result.text == c_result_data[1]

""" TC03 - Üres kitöltés:
	a: <üres>
	b: <üres>
	c: NaN"""

def test_clear_data():
    a_input.clear()
    b_input.clear()
    submit_button.click()
    assert result.text == c_result_data[2]

    driver.close()