import pytest
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class TestShoppingCartCoffe:     
         
    def test_should_add_to_card(self):
        web = Chrome()
        web.implicitly_wait(10)
        wait = WebDriverWait(web,3)
        web.get('https://coffee-cart.app/')
        coffee_cups = web.find_elements(By.CSS_SELECTOR,'li:has(.cup)')     
        lista_precios =[]
        for n in range(0,3):
            index = random.randint(0,len(coffee_cups)-1)
            given_coffee = coffee_cups[index]
            price = given_coffee.find_element(By.CSS_SELECTOR,'small').text
            price =float(price.replace("$",""))
            lista_precios.append(price)
            ActionChains(web).move_to_element(given_coffee).perform()   
            wait.until(lambda web: visibility_of_element_located(given_coffee))      
            given_coffee.click()
         
                   
        total = sum(lista_precios) 
        total = f"{total:.2f}"        
        expected_total = f"Total: ${total}"      
        button_total_coffe = web.find_element(By.CSS_SELECTOR,'[data-test="checkout"]').text
        assert button_total_coffe == expected_total
       
        
        

if __name__ == "__main__":  
    pytest.main()       