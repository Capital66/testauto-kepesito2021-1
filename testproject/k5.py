from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)

""" TC01 -	Az applikáció helyesen megjelenik:
o	A bingo tábla 25 darab cellát tartalmaz
o	A számlista 75 számot tartalmaz"""


def test_good_bingo():
    cells = driver.find_elements_by_name("number")
    assert len(cells) == 25

    elements_number = driver.find_elements_by_xpath('//*[@id="numbers-list"]/li/input')
    assert len(elements_number) == 75

    driver.close()


""" TC02 -	Bingo számok ellenőzrzése:
o	Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
o	Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki"""

play_button = driver.find_elements_by_id("spin")
play_button.click()


""" TC03 - Új játékot tudunk indítani
o	az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
o	új bingo szelvényt kapunk más számokkal."""
