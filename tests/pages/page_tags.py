import random
from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@dataclass
class TestTagsInputBoxPage:
    driver: WebDriver

    def __post_init__(self):
        self.container_tags = self.driver.find_elements(By.CSS_SELECTOR, '.content li')
        self.input_file = self.driver.find_element(By.CSS_SELECTOR, '.content input')
        self.button_delete_all = self.driver.find_element(By.CSS_SELECTOR, '.details button')
        self.message = self.driver.find_element(By.CSS_SELECTOR, '.details span')

    def add_tags_in_container(self):
        tabs_count = len(self.container_tags)
        new_tab = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]

        if tabs_count > 0:
            index_tabs = random.randint(tabs_count + 1, 8)
            elements_tags = new_tab[:index_tabs]
            for index in range(index_tabs):
                self.input_file.send_keys(elements_tags[index])
                self.input_file.send_keys(Keys.ENTER)

    def delete_all_tags_in_container(self):
        button_delete = self.button_delete_all
        button_delete.click()

    def remove_a_tag_in_container(self):
        tabs_count = len(self.container_tags)
        if tabs_count > 0:
            index_tabs = random.randint(1, tabs_count)

            for index in range(index_tabs):
                self.input_file.send_keys(elements_tags[index])
                self.input_file.send_keys(Keys.ENTER)
