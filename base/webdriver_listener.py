import pytest
from selenium import webdriver
from utilities import read_utils


class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        browser_name = read_utils.get_value_from_json("../test_data/data.json", "browser")

        if browser_name == "Edge":
            self.driver = webdriver.Edge()

        elif browser_name == "FF":
            self.driver = webdriver.Firefox()

        else:
            self.driver = webdriver.Chrome()
        # service = Service(executable_path==r"<filepath_of_chrome>")
        # driver = webdriver.Chrome(Service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()
