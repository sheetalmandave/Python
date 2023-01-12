import time

from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    shopping_cart_link = (By.LINK_TEXT, "shopping cart")
    proceed_to_checkout = (By.XPATH, "//span[text()='Proceed to Checkout']")
    customer_email_locator = "customer-email"
    customer_email = (By.ID, "customer-email")
    first_name = (By.XPATH, "//*[@name='firstname']")
    last_name = (By.XPATH, "//*[@name='lastname']")
    company_name = (By.XPATH, "//*[@name='company']")
    street_1 = (By.XPATH, "//*[@name='street[0]']")
    street_2 =(By.XPATH, "//*[@name='street[1]']")
    street_3 = (By.XPATH, "//*[@name='street[2]']")
    city_name = (By.XPATH, "//*[@name='city']")
    region_id = "//*[@name='region_id']"
    telephone_no = (By.XPATH, "//*[@name='telephone']")
    shipping_method = (By.XPATH, "(//input[@type='radio'])[1]")
    next_btn = (By.XPATH, "//span[text()='Next']")


    postal_code = (By.XPATH, "//*[@name='postcode']")

    def click_on_shopping_cart_link(self):
        return self.driver.find_element(*CheckoutPage.shopping_cart_link).click()

    def click_on_pcheckout(self):
        return self.driver.find_element(*CheckoutPage.proceed_to_checkout).click()

    def enter_customer_email(self, value):
        return self.driver.find_element(*CheckoutPage.customer_email).send_keys(value)

    def enter_first_name(self, value):
        return self.driver.find_element(*CheckoutPage.first_name).send_keys(value)

    def enter_last_name(self, value):
        return self.driver.find_element(*CheckoutPage.last_name).send_keys(value)

    def enter_company_name(self, value):
        return self.driver.find_element(*CheckoutPage.company_name).send_keys(value)

    def enter_street_1(self, value):
        return self.driver.find_element(*CheckoutPage.street_1).send_keys(value)

    def enter_street_2(self, value):
        return self.driver.find_element(*CheckoutPage.street_2).send_keys(value)

    def enter_street_3(self, value):
        return self.driver.find_element(*CheckoutPage.street_3).send_keys(value)

    def enter_city_name(self, value):
        return self.driver.find_element(*CheckoutPage.city_name).send_keys(value)

    def enter_postal_code(self, value):
        return self.driver.find_element(*CheckoutPage.postal_code).send_keys(value)

    def enter_telephone_no(self, value):
        return self.driver.find_element(*CheckoutPage.telephone_no).send_keys(value)

    def select_shipping_method(self):
        return self.driver.find_element(*CheckoutPage.shipping_method).click()

    def click_on_next(self):
        return self.driver.find_element(*CheckoutPage.next_btn).click()