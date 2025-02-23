import time


from selenium.webdriver.common.by import By
import pytest
from conftest import driver



class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [
        ('Malviviente', 'Password123',"Your username is invalid!" ),
        ('student', 'JAJAJA', "Your password is invalid!")])         #sintaxis de parametro ("name1, name2, name3",[("param1", "param2", "param3),("param2.1", "param2.2", "param2.3")]
    def test_negative_login(self, driver, username, password, expected_error_message  ):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys(username)
        time.sleep(1)
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, 'password')
        password_locator.send_keys(password)
        time.sleep(1)
        # Push Submit button
        submit_button_locator = driver.find_element(By.ID, 'submit')
        submit_button_locator.click()
        time.sleep(1)
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, 'error')
        assert error_locator.is_displayed(), "error message is not displayed"
        # Verify error message text is Your username is invalid!
        error_text = error_locator.text
        assert error_text == expected_error_message, "message should be: Your username is invalid!"
        time.sleep(1)
        """
        Test case 2: Negative username test
        Open page
        Type username incorrectUser into Username field
        Type password Password123 into Password field
        Push Submit button
        Verify error message is displayed
        Verify error message text is Your username is invalid!
        """



    def test_login_username_negative(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        #Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, 'username' )
        username_locator.send_keys('Malviviente')
        time.sleep(1)
        #Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, 'password')
        password_locator.send_keys('Password123')
        time.sleep(1)
        #Push Submit button
        submit_button_locator = driver.find_element(By.ID, 'submit')
        submit_button_locator.click()
        time.sleep(1)
        #Verify error message is displayed
        error_locator = driver.find_element(By.ID, 'error')
        assert error_locator.is_displayed(), "error message is not displayed"
        #Verify error message text is Your username is invalid!
        error_text = error_locator.text
        assert error_text == "Your username is invalid!", "message should be: Your username is invalid!"
        time.sleep(1)
        """
        Test case 2: Negative username test
        Open page
        Type username incorrectUser into Username field
        Type password Password123 into Password field
        Push Submit button
        Verify error message is displayed
        Verify error message text is Your username is invalid!
        """


    def test_login_password_negative(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        #Type username student into Username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('student')
        #Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, 'password')
        password_locator.send_keys('JAJAJA')
        #Push Submit button
        submit_button_selector = driver.find_element(By.ID, 'submit')
        submit_button_selector.click()
        #Verify error message is displayed
        error_locator = driver.find_element(By.ID, 'error')
        assert error_locator.is_displayed(), "No se mostro error"
        #Verify error message text is Your password is invalid!"""
        error_text = error_locator.text
        assert error_text == "Your password is invalid!", "Should be: Your password is invalid!"


        """Open page
Type username student into Username field
Type password incorrectPassword into Password field
Push Submit button
Verify error message is displayed
Verify error message text is Your password is invalid!"""