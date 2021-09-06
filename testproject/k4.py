from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)

""" TC01 -	Helyesen betöltődik az applikáció:
o	Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
	!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

chrs_line = driver.find_element_by_xpath("/html/body/div/div/p[3]")

""" TC02 -	Megjelenik egy érvényes művelet:
o	chr mező egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
o	op mező vagy + vagy - karaktert tartlamaz
o	num mező egy egész számot tartalamaz"""


def test_good_chr():
    chr_field = driver.find_element_by_id("chr")
    op_field = driver.find_element_by_id("op")
    num_field = driver.find_element_by_id("num")
    assert int(num_field.text) == int()

    driver.close()

""" TC03 -	Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
o	A megjelenő chr mezőben lévő karaktert kikeresve a táblában
o	Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
o	A num mezőben megjelenő mennyiségű karaktert
o	az result mező helyes karaktert fog mutatni"""


