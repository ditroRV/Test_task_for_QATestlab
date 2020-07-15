from BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from datetime import date


class SearchResultsLocators():
    LOCATOR_HOTELS_LIST = (By.XPATH, "//span[@class='bui-button__text']")
    LOCATOR_SUBMIT_BUTTON = (By.CLASS_NAME, "sb-searchbox__button ")
    LOCATOR_LIST_OF_PRICES = (By.XPATH, "//div[@class='bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper']")
    CALENDAR_XPATH = ("//div[@class='c2-calendar']")
    CALENDAR_CLASS_NAME = 'bui-calendar__display'
    LOCATOR_TODAY_DATE = "//div[contains(@class, 'calendar')]//span[contains(text()"


class SearchResults(BasePage):
    def get_calendar_text(self):
        return LOCATOR_CALENDAR_LABEL.text

    def get_price_from_list(self,price_list,list_index):
         price = price_list[list_index].text.split(" ")[1]
         return price


    def go_to_any_hotel_and_click_show_prices(self):

       any_hotel_index = BasePage.random_index(SearchResultsLocators.LOCATOR_HOTELS_LIST)
       self.find_elements(SearchResultsLocators.LOCATOR_HOTELS_LIST)[any_hotel_index].click()

    def get_calendar_xpath(self):
        print(SearchResultsLocators.CALENDAR_XPATH)
        return SearchResultsLocators.CALENDAR_XPATH

    def get_calendar_clas_name(self):
        print(SearchResultsLocators.CALENDAR_CLASS_NAME)
        return SearchResultsLocators.CALENDAR_CLASS_NAME


    def get_today_date(self):
        today = date.today()
        return today.strftime("%d")

    def set_any_dates(self):
        today_date = self.driver.find_element_by_xpath(f"{SearchResultsLocators.LOCATOR_TODAY_DATE}, '{self.get_today_date()}')]")
        today_date.click()


    def click_submit_button(self):
        self.find_element(SearchResultsLocators.LOCATOR_SUBMIT_BUTTON).click()

    def prices_elements(self):
        list_of_prices = self.find_elements(SearchResultsLocators.LOCATOR_LIST_OF_PRICES)
        return list_of_prices

    def prices(self):
        self.prices_elements()
        return map(lambda e: self.get_price_from_price_element(e),self.prices_elements())

    def  get_prices_list_length(self):
        list_of_prices = self.find_elements(SearchResultsLocators.LOCATOR_LIST_OF_PRICES)
        prices_list_length = len(list_of_prices[0].text)
        return prices_list_length

    def get_price_from_price_element(self,price_element):
        return price_element.text.split(" ")[1]


    def set_date_and_click_submit_button(self):
        self.set_any_dates()
        self.click_submit_button()


    def is_firtst_calendar_displayed(self):
        is_calendar_displayed = self.is_element_displayed(self.get_calendar_xpath())
        return is_calendar_displayed


    def is_second_calendar_displayed(self):
        is_calendar_displayed =  self.is_element_displayed_by_class_name(self.get_calendar_clas_name())
        return is_calendar_displayed

    def is_calendars_displayed(self):
        if self.is_firtst_calendar_displayed or self.is_second_calendar_displayed():
            return True
        else:
            return False


    def is_price_displayed(self):
        prices_list = self.prices_elements()
        prices = self.prices()
        for price in prices:
            if len(price) > 0:
                return True
            else:
                return False