import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver


@pytest.mark.usefixtures("setup")
class TestSearchFlightsAndVerifyFilter:
    def test_searchflights(self):
        wait = WebDriverWait.until()
        depart_from = driver.find(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)





