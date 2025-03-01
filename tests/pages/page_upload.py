from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


@dataclass
class TestUploadPage:
    driver: WebDriver

    def __post_init__(self):
        self.button_file_input = lambda: self.driver.find_element(By.ID, 'file-input')
        self.etiquette_file = lambda: self.driver.find_element(By.ID, 'num-of-files')

    def upload_file(self, file_path):
        btn = self.button_file_input()
        btn.send_keys(file_path)
