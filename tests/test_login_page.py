import pytest

from conftest import driver
from page_object.login_page import LoginPage
from page_object.login_succesfully import LoginSuccessfullyPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Test case 1: Positive LogIn test
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login('student', 'Password123')
        login_successfully_page = LoginSuccessfullyPage(driver)
        assert login_successfully_page.expected_url == login_successfully_page.current_url, "Actual URL is not expected"
        assert 'Congratulations' or 'successfully logged in' in login_successfully_page.header_text, "Text not expected"
        assert login_successfully_page.is_logout_button_display(), "Log out button not displayed"


        # #Type username student into Username field
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        #
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys(username)
        #
        # #Type password Password123 into Password field
        # password_locator = driver.find_element(By.NAME, "password")
        # password_locator.send_keys(password)
        #
        # #Push Submit button
        # btn_submit_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        # btn_submit_locator.click()
        #
        # #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # actual_url = driver.current_url
        #
        # assert expected_url in actual_url
        #
        #
        # #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # text_locator = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/p[1]/strong')
        # actual_text = text_locator.text
        #
        # assert expected_message in actual_text
        #
        # #Verify button Log out is displayed on the new page
        # btn_logout_locator = driver.find_element(By.LINK_TEXT, 'Log out')
        # assert btn_logout_locator.is_displayed()
        """
        Test case 1: Positive LogIn test
        Open page
        Type username student into Username field
        Type password Password123 into Password field
        Push Submit button
        Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        Verify button Log out is displayed on the new page
        
        """