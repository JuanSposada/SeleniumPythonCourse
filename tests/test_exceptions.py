import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver


class TestExceptions:

    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, 'add_btn')
        add_button_locator.click()
        # Verify Row 2 input field is displayed
        # driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="row2"]/input')))
        assert row2_input_element.is_displayed(), "Row 2 is not displayed"

    @pytest.mark.exception
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, 'add_btn')
        add_button_locator.click()
        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="row2"]/input')))
        # Type text into the second input field
        row2_input_element.send_keys('Sushi')
        # Push Save button using locator By.name(“Save”)
        # save_button_locator = driver.find_element(By.NAME,"Save")
        # save_button_locator.click()
        driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']").click()
        # Verify text saved
        # saved_food_text = driver.find_element(By.ID, "confirmation").text
        saved_confirmation = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        saved_food_text = saved_confirmation.text
        assert saved_food_text == "Row 2 was saved", "no se guardo"

    @pytest.mark.exception
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Clear input field
        first_input_locator = driver.find_element(By.XPATH, '//*[@id="row1"]/input')
        driver.find_element(By.ID, "edit_btn").click()
        wait = WebDriverWait(driver, 1)
        wait.until(ec.element_to_be_clickable(first_input_locator))
        first_input_locator.clear()
        # Type text into the input field
        first_input_locator.send_keys("Ramen")
        # Verify text changed
        driver.find_element(By.XPATH, "//button[@id='save_btn']").click()
        # saved_confirmation = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # saved_food_text = saved_confirmation.text
        assert wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))

    @pytest.mark.exception
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Find the instructions text element
        instructions_locator = driver.find_element(By.ID, "instructions")
        # Push add button
        driver.find_element(By.ID, 'add_btn').click()
        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, 'add_btn')), "should not displayed")

    @pytest.mark.exception
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        driver.find_element(By.ID, "add_btn").click()
        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 7)
        row2_input_locator = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
                                        "failed loading before 3 secs")
        # Verify second input field is displayed
        assert row2_input_locator.is_displayed()