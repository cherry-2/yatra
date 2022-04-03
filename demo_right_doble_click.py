from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoRightDouble:
    def demo_right_doubleclick(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        action_chain = ActionChains(driver)
        right_click = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        action_chain.context_click(right_click).perform()
        sleep(2)
        rclick = driver.find_element(By.XPATH, "//span[normalize-space()='Delete']")
        rclick.click()
        sleep(4)
        alert = driver.switch_to.alert
        alert.accept()
        sleep(4)
        d_click = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        action_chain.double_click(d_click).perform()
        sleep(6)


dright = DemoRightDouble()
dright.demo_right_doubleclick()
