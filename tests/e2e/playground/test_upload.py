import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.pages.page_upload import TestUploadPage


class TestUpdate:
    def test_should_upload_a_file_successfully(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/upload/')
        test_uploadfile = TestUploadPage(driver)
        file_path = os.path.abspath("1212.jpg")
        test_uploadfile.upload_file(file_path)
        time.sleep(3)
        texto_infor = test_uploadfile.etiquette_file().text
        assert "File Selected" in texto_infor


if __name__ == "__main__":
    pytest.main()
