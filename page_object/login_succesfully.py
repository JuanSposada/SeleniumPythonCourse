from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginSuccessfullyPage:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/p[1]/strong')
    __logout_button = (By.LINK_TEXT, 'Log out')


    def __init__(self, driver: WebDriver):
        self._driver = driver


    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header_text(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    def is_logout_button_display(self) -> bool:
        return self._driver.find_element(self.__logout_button).is_displayed()



