import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestDownload:
    def test_should_dowload_a_file_successfully(self):
        driver = webdriver.Chrome
        driver.get("https://qaplayground.dev/apps/download/")


if __name__ == "__main__":
    pytest.main()
