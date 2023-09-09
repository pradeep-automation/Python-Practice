import pytest
from SingletonDriverExample.WebDriverSingleton.webdriversingleton import WebDriverSingleton


@pytest.fixture(scope="module")
def singleton_driver():
    instance = WebDriverSingleton()
    yield instance
    instance.close_driver()


def test_example(singleton_driver):
    driver = singleton_driver.get_driver()
    driver.get("https://www.google.com")



