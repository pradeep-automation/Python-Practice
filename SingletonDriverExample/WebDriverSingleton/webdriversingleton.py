from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = webdriver.Chrome()
        return cls._instance

    def get_driver(self):
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None





