from selenium import webdriver
import sqlite3
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Parser():
    def __init__(self, base, url):
        self.base = base
        self.url = url

    def setup(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1,1")
        self.driver = webdriver.Chrome(options=self.options)
        with sqlite3.connect(f"{self.base}.sqlite3") as db:
            cursor = db.cursor()
            cursor.executescript(
                '''CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY , count INTEGER, date DATE)''')
    def parse(self):
        self.driver.get(self.url)
        el = self.driver.find_element(By.CLASS_NAME, 'rts-counter')

        count = int(el.text.replace(',',''))
        date = str(datetime.date.today())
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'rts-counter')))
        self.driver.quit()
        with sqlite3.connect(f"{self.base}.sqlite3") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO data(count, date) VALUES(?, ?)", (count, date))
