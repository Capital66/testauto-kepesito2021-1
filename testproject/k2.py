from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)

""" TC01 - Helyesen jelenik meg az applikáció betöltéskor:
o	Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
 A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]"""


def test_good_app_color():
    random_color = driver.find_element_by_id("randomColor")
    assert random_color.is_displayed() == True
    result_color = driver.find_element_by_id("testColor")
    assert result_color.is_displayed() == False


"""TC02 - El lehet indítani a játékot a start gommbal.
o	Ha elindult a játék akkor a stop gombbal le lehet állítani."""

start_button = driver.find_element_by_id("start")
start_button.click()
stop_button = driver.find_element_by_id("stop")
stop_button.click()

"""TC03 - Eltaláltam, vagy nem találtam el.
o	Ha leállítom a játékot két helyes működés van,
 ha akkor állítom épp le amikor a bal és a jobb oldal ugyan azt a színt tartalmazza
  akkor a Correct! felirat jelenik meg. ha akkor amikor eltérő szín van a jobb és bal oldalon
   akkor az Incorrect! felirat kell megjelenjen."""


def test_use_color():
    start_button.click()
    stop_button.click()
    random_color_name = driver.find_element_by_id("randomColorName")
    test_color_name = driver.find_element_by_id("testColorName")
    result = driver.find_element_by_id("result")
    if (random_color_name.text == test_color_name.text):
        assert result.text == "Correct!"
    if (random_color_name.text != test_color_name.text):
        assert result.text == "Incorrect!"

    driver.close()
