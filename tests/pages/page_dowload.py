from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


@dataclass
class TestDownloadPage:
    driver: WebDriver

    def __post_init__(self):
        self.button_file_download = lambda: self.driver.find_element(By.ID, 'file')

    def download_file(self):
        bnc = self.button_file_download()
        bnc.click()
