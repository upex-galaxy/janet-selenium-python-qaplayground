import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLogin:
    def test_1_should_login_successfull_with_valid_credentials(self):
        """GX3-2323: Deberia iniciar sesion con credenciales validas"""
        web = WebDriver()
        web.get('https://www.saucedemo.com/')
        username_input = web.find_element(By.CSS_SELECTOR,'[data-test="username"]')
        username_input.send_keys('standard_user')
        password_input = web.find_element(By.CSS_SELECTOR,'[data-test="password"]')
        password_input.send_keys('secret_sauce')
        login_button = web.find_element(By.CSS_SELECTOR,'[data-test="login-button"]')
        login_button.click()
        pass
     
                   
if __name__ == "__main__":
    pytest.main()