from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoSwitchWindows:
    def switch_windows(self):
        global child_handle
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        print(driver.title)
        print(driver.current_url)
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                child_handle = driver.current_window_handle
                driver.find_element(By.XPATH, "//span[normalize-space()='Singapore Airlines']").click()
                break
        handles = driver.window_handles
        for handle in handles:
            if handle == parent_handle:
                pass
            elif handle == child_handle:
                pass
            else:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("cherry")
                break
        driver.switch_to.window(parent_handle)


d_multiple = DemoSwitchWindows()
d_multiple.switch_windows()



