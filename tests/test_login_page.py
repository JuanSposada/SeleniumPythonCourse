import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from conftest import driver



class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize('username, password, expected_url, expected_message',
                             [ ('student', 'Password123',"practicetestautomation.com/logged-in-successfully/", 'Congratulations' )])

    def test_positive_login(self, driver, username, password, expected_url, expected_message):

        #Type username student into Username field
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        #Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        #Push Submit button
        btn_submit_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        btn_submit_locator.click()

        #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url

        assert expected_url in actual_url


        #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/p[1]/strong')
        actual_text = text_locator.text

        assert expected_message in actual_text

        #Verify button Log out is displayed on the new page
        btn_logout_locator = driver.find_element(By.LINK_TEXT, 'Log out')
        assert btn_logout_locator.is_displayed()
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