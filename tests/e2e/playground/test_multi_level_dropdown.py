import pytest
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.pages.page_multilevel import TestMultilevelPage


class TestMultilevelDropdown:

    def test_should_open_a_menu_option(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/multi-level-dropdown/#settings')
        test_multilevel = TestMultilevelPage(driver)
        test_multilevel.select_navigations_buttons()
        selected = test_multilevel.select_menu_items()
        menu_selec = selected.strip().replace('🦧\n', '').lower()
        url = driver.current_url
        assert menu_selec in url

    def test_should_open_a_specific_menu(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/multi-level-dropdown/#settings')
        test_multilevel = TestMultilevelPage(driver)
        test_multilevel.select_navigations_buttons()
        selected = test_multilevel.select_menu_items()
        menu_selec = selected.strip().replace('🦧\n', '').lower()
        url = driver.current_url
        if menu_selec in url:
            test_multilevel.select_menu_items()
            assert menu_selec in url


if __name__ == "__main__":
    pytest.main()
