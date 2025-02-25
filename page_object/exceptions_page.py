from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class ExceptionsPage(BasePage):
    #Locators
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, 'add_btn')
    __first_input_locator = (By.XPATH, '//*[@id="row1"]/input')
    __row2_input_locator = (By.XPATH, '//*[@id="row2"]/input')
    __save2_button = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")
    __confirmation_saved = (By.ID, "confirmation")
    __edit_button = (By.ID, "edit_btn")
    __instructions_locator = (By.ID, "instructions")
    __save_button = (By.XPATH, "//button[@id='save_btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row2_input_locator)

    def add_second_food(self, text):
        super()._type(self.__row2_input_locator, text)
        super()._click(self.__save2_button)
        super()._wait_until_element_is_visible(self.__confirmation_saved)

    def modify_first_input(self, text):
        super()._click(self.__edit_button)
        super()._wait_until_element_is_clickable(self.__first_input_locator)
        super()._clear_input(self.__first_input_locator)
        super()._type(self.__first_input_locator, text)
        super()._click(self.__save_button)
        super()._wait_until_element_is_visible(self.__confirmation_saved)


    def add_type_save_second_row(self, text):
        self.add_second_row()
        super()._type(self.__row2_input_locator, text)
        super()._click(self.__save2_button)


    def click_add_button(self):
        super()._find(self.__add_button_locator).click()

    def is_row2_input_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__row2_input_locator)
        return super()._is_displayed(self.__row2_input_locator)

    def type_input_2(self, text: str):
        super()._type(self.__row2_input_locator, text)

    def type_input_1(self, text: str):
        super()._type(self.__first_input_locator, text)

    def click_save_button(self):
        super()._click(self.__save_button)

    def click_save_button2(self):
        super()._click(self.__save2_button)

    def is_saved(self) -> bool:
        return super()._is_displayed(self.__confirmation_saved)

    def input1_clear(self):
        super()._clear_input(self.__first_input_locator)

    def click_edit_button(self):
        super()._click(self.__edit_button)

    def is_instruction_displayed(self) -> bool:
        return super()._is_displayed(self.__instructions_locator)

    def get_confirmation_message(self) -> str:
        return super()._get_text(self.__confirmation_saved)




