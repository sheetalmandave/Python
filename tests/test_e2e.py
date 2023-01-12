from selenium.webdriver import ActionChains
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilitiy.BaseClass import BaseClass
from PageObject.homePage import HomePage
from PageObject.checkoutPage import CheckoutPage
from PageObject.placeOrder import PlaceOrder


class TestPom(BaseClass):
    def test_navigateToHome(self):
        log = self.getLogger()
        homepageobj = HomePage(self.driver)
        time.sleep(5)
        action = ActionChains(self.driver)
        time.sleep(5)
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, homepageobj.gear_path)).perform()
        log.info("Mouse hovered on Gear dropdown")
        time.sleep(5)
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, homepageobj.bag_path)).click().perform()
        log.info("clicked on Bags button")

    def test_addtocart(self):
        log = self.getLogger()
        homepageobj = HomePage(self.driver)
        homepageobj.click_on_add_cart()
        log.info("clicked on Bag")
        homepageobj.click_on_add_cart_span()
        log.info("clicked on Add to cart")

    def test_proceedCheckout(self):
        log = self.getLogger()
        checkoutobj = CheckoutPage(self.driver)
        time.sleep(10)
        checkoutobj.click_on_shopping_cart_link()
        checkoutobj.click_on_pcheckout()
        log.info("clicked on Proceed to checkout")
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, checkoutobj.customer_email_locator)))
        checkoutobj.enter_customer_email("abc@testetst.com")
        log.info("Entered Customer email Id")
        time.sleep(1)
        checkoutobj.enter_first_name("abc")
        log.info("Entered first name")
        time.sleep(1)
        checkoutobj.enter_last_name("xyz")
        log.info("Entered last name")
        time.sleep(1)
        checkoutobj.enter_company_name("company")
        log.info("Entered company Name")
        time.sleep(1)
        checkoutobj.enter_street_1("street line1")
        log.info("Entered street1 name")
        time.sleep(1)
        checkoutobj.enter_street_2("street line2")
        log.info("Entered street2 name")
        time.sleep(1)
        checkoutobj.enter_street_3("street line3")
        log.info("Entered street3 name")
        time.sleep(1)
        checkoutobj.enter_city_name("Aurangabad")
        log.info("Entered city name")
        time.sleep(1)
        self.select_valuefrom_dropdown(checkoutobj.region_id, "47")
        log.info("selected regionId from the dropdown")
        checkoutobj.enter_postal_code("431003")
        log.info("Entered postal code")
        time.sleep(1)
        checkoutobj.enter_telephone_no("1234567891")
        log.info("Entered telephone number")
        time.sleep(5)
        checkoutobj.select_shipping_method()
        time.sleep(5)
        checkoutobj.click_on_next()
        log.info("Clicked on Next button")
        time.sleep(10)

    def test_placeOrder(self):
        log = self.getLogger()
        # "Place Order"
        placeorderobj = PlaceOrder(self.driver)
        placeorderobj.click_on_placeorder()
        log.info("Clicked on Place Order")
        time.sleep(3)
        # Print order number and take screenshot
        self.driver.implicitly_wait(5)
        print(self.driver.find_element(By.XPATH, placeorderobj.order_number).text)
        self.driver.get_screenshot_as_file("order.png")
