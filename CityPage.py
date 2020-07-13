from BasePage import BasePage
from selenium.webdriver.common.by import By

class CityPageLocators():
    LOCATOR_LOWER_PRICE_FIRST = (By.XPATH, "//div[@class='content__nav']/span[2]")
    LOCATOR_HOTEL_HEADER = (By.XPATH, "//h2[@class='sr-snippet__header']")
    LOCATOR_CALENDAR_LABEL = (By.CLASS_NAME, 'bui-calendar__display')
    BOOKING_STATUS_XPATH = '//*[@id="hotellist_inner"]/div[1]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div[3]/div'



class CityPage(BasePage):
    def get_hotel_header(self):
      return  self.find_element(CityPageLocators.LOCATOR_HOTEL_HEADER)

    def get_calendar_text(self):
        calendar_label = self.find_element(CityPageLocators.LOCATOR_CALENDAR_LABEL)
        return calendar_label.text

    def get_booking_status_xpath(self):
        return CityPageLocators.BOOKING_STATUS_XPATH

    def click_on_lower_prices_first_tab(self):
        return self.find_element(CityPageLocators.LOCATOR_LOWER_PRICE_FIRST).click()
