import os
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOpt
from dotenv import load_dotenv

load_dotenv()

ON_CI = os.getenv('CI') == 'true'


@pytest.fixture
def web():
    options = ChromeOpt()
    if ON_CI:
        options.add_argument("--headless")

    web = Chrome(options=options)
    return web
