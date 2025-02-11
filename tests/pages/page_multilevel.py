from dataclasses import dataclass
import sys
import random
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@dataclass
class TestMultilevelPage:
    driver: WebDriver

    def __post_init__(self):
        self.navigation_buttons = lambda: self.driver.find_elements(By.CLASS_NAME, 'icon-button')
        self.menu_items = lambda: self.driver.find_elements(By.CLASS_NAME, 'menu-item')

    def select_navigations_buttons(self):
        ##WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.navigation_buttons))
        btn = self.navigation_buttons()
        btn[3].click()

    def select_menu_items(self):
        nro_lista = len(self.menu_items())
        index_dd = random.randint(1, nro_lista)
        item_selc = self.menu_items()[index_dd]
        item_selc_text = item_selc.text
        item_selc.click()
        return item_selc_text
