import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    # if request.params == "chrome":
    #     web_driver = webdriver.Chrome(ChromeDriverManager().install())
    # if request.params == "firefox":
    #     web_driver = webdriver.Firefox(GeckoDriverManager().install())
    # request.cls.driver = web_driver
    web_driver = webdriver.Chrome(executable_path=TestData.EXECUTABLE_PATH)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()
