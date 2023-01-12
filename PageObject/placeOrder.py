import time

from selenium.webdriver.common.by import By


class PlaceOrder:
    def __init__(self, driver):
        self.driver = driver

    place_order = (By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button')  #("//span[text()='Place Order']")
    order_number = "//*[@class='checkout-success']/p[1]"

    def click_on_placeorder(self):
        return self.driver.find_element(*PlaceOrder.place_order).click()