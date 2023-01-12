import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    gear_path ='[id="ui-id-6"]'
    bag_path = "Bags"
    time.sleep(3)
    add_cart = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[4]/div/a/span/span/img')
    addcart_span =(By.XPATH, '//*[@id="product-addtocart-button"]/span')
    checkout_page = (By.XPATH, "//*[@data-role='proceed-to-checkout']")

    def click_on_add_cart(self):
        return self.driver.find_element(*HomePage.add_cart).click()

    def click_on_add_cart_span(self):
        return self.driver.find_element(*HomePage.addcart_span).click()



