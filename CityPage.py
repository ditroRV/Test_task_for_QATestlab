from BasePage import BasePage
from selenium.webdriver.common.by import By

class CityPageLocators():
    LOCATOR_LOWER_PRICE_FIRST = (By.XPATH, "//div[@class='content__nav']/span[2]")
    LOCATOR_HOTEL_HEADER = (By.XPATH, "//h2[@class='sr-snippet__header']")
    LOCATOR_CALENDAR_LABEL = (By.CLASS_NAME, 'bui-calendar__display')
    LOCATOR_AVERAGE_PRICE_NIGHT = (By.XPATH,"//div[@class='sr__card_price bui-spacer--large'][contains(text(), 'Avg. price/night:')]")
    LOCATOR_HOTEL_INFO = (By.CLASS_NAME,"sr__card_review")


class CityPage(BasePage):
    def get_hotel_header(self):
      return  self.find_element(CityPageLocators.LOCATOR_HOTEL_HEADER)

    def get_calendar_text(self):
        calendar_label = self.find_element(CityPageLocators.LOCATOR_CALENDAR_LABEL)
        return calendar_label.text

    def click_on_lower_prices_first_tab(self):
        return self.find_element(CityPageLocators.LOCATOR_LOWER_PRICE_FIRST).click()

    def hotels_list(self):
        list_of_hotels = self.find_elements(CityPageLocators.LOCATOR_AVERAGE_PRICE_NIGHT)
        return list_of_hotels
