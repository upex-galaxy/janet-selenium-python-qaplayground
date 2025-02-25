from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


@dataclass
class TestDownloadPage:
    driver: WebDriver

    def __post_init__(self):
        self.button_file_download = lambda: self.driver.find_element(By.ID, 'file')

    def upload_file(self, file_path):
        self.button_file_download().click()
