from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.base_url = "https://www.booking.com/"


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


    def go_to_site(self):
        return self.driver.get("https://www.booking.com/")


    def random_index(end):
        if isinstance(end, int):
            return random.randint(0, end - 1)
        else:
            return random.randint(0, len(end) - 1)


    def  element_is_not_displayed(self,xpath):
        print(f'========================================================================={xpath}')
        if len(self.driver.find_elements(xpath)):
            return False
        else:
            return True


    def is_element_displayed(self,xpath):
        if len(self.driver.find_elements_by_xpath(xpath)):
            return True
        else:
            return False


    def is_element_displayed_by_class_name(self,class_name):
        if len(self.driver.find_elements_by_class_name(class_name)):
            return True
        else:
            return False