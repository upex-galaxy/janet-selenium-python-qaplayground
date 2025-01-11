import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class TestClosePopups:
    def test_should_display_message_when_closing_popup(self):
        web = Chrome()
        web.get('https://qaplayground.dev/apps/onboarding-modal/#')
        menu_button = web.find_element(By.CSS_SELECTOR,'.menu-btn')
        menu_button.click()
        message_final = web.find_element(By.CSS_SELECTOR,'[class="title"]').text
        assert 'Welcome Peter Parker!' in message_final

        






if __name__ == "__main__":  
    pytest.main()   