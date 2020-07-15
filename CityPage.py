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

    def is_page_title_corect(self,homepage_object):
        expected_title = f'Hotels and More in {homepage_object}'
        if self.get_hotel_header().text == expected_title:
            return True;
        else:
            return False


    def is_calendar_open_for_specifying(self):
        if self.get_calendar_text() == 'Check-in - Check-out':
            return True
        else:
            return False

    def is_no_result_entry_containing_booking_price_or_booking_status(self):
        hotels = self.hotels_list()
        for hotel in hotels:
            if 'Avg. price/night' in hotel.text and 'nights' not in hotels:
                return True
            else:
                return False