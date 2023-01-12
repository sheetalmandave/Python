import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def select_valuefrom_dropdown(self, locator, value):
        dropdown = Select(self.driver.find_element(By.XPATH, locator))
        dropdown.select_by_value(value)