from BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from datetime import date


class SearchResultsLocators():
    LOCATOR_HOTELS_LIST = (By.XPATH, "//span[@class='bui-button__text']")
    LOCATOR_SUBMIT_BUTTON = (By.CLASS_NAME, "sb-searchbox__button ")
    LOCATOR_LIST_OF_PRICES = (By.XPATH, "//div[@class='bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper']")
    LOCATOR_BOOKING_PRICES = (By.XPATH, '//*[@id="hotellist_inner"]/div[1]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div')
    CALENDAR_XPATH = ("//div[@class='c2-calendar']")
    CALENDAR_CLASS_NAME = 'bui-calendar__display'



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
        #today_date = driver.find_element_by_class_name("bui-calendar__date bui-calendar__date--today")
        today_date = self.driver.find_element_by_xpath(f"//div[contains(@class, 'calendar')]//span[contains(text(), '{self.get_today_date()}')]")
        print(f'today date {today_date.text}')
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


    def search_any_date(self):
        self.set_any_dates()
        self.click_submit_button()