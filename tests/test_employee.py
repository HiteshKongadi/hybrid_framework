import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):
    @pytest.mark.parametrize("username,password,firstname,middlename,lastname,exp_profile_header,exp_firstname",
                             data_source.test_employee_data)
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, exp_profile_header,
                                exp_firstname):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.XPATH, "// button[ @ type = 'submit']").click()
        # assert isinstance(self.driver.find_element(By.XPATH, "//div[contains(@class,'employee-name')]").text, object)
        time.sleep(10)
        actual_employee_name = self.driver.find_element(By.XPATH, "//div[contains(@class,'employee-name')]").text
        assert_that(exp_profile_header).is_equal_to(actual_employee_name)
        # time.sleep(5)
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(exp_firstname).is_equal_to(actual_first_name)

    @pytest.mark.parametrize("username,password,file_path,expected_error",
                             data_source.test_invalid_file_type)
    def test_add_invalid_file_type(self, username, password, file_path, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        wait = WebDriverWait(self.driver, 30)
        #wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.NAME, "firstName"), "value", firstname))
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        actual_error = self.driver.find_element(By.XPATH,
                                                f"//span[contains(normalize-space(),'{expected_error}')]").text
        assert_that(actual_error).is_equal_to(expected_error)
        #   print("add valid employee")
