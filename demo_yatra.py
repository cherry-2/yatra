from time import sleep
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class DemoYatra:
    def demo_yatra(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        watch =WebDriverWait(driver, 10)

        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        origin = watch.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        origin.click()
        origin.send_keys("New Delhi")
        sleep(5)
        alert = driver.switch_to.alert
        alert.dismiss()
        sleep(5)
        destination = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        destination.send_keys("Goa")
        # destination.click()
        driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        all_dates = driver.find_elements(By.XPATH, "//div[@class='month-wrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "22/02/2022":
                date.click()
                break
        driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
        sleep(5)


dy = DemoYatra()
dy.demo_yatra()
