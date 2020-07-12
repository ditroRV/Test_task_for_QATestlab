import pytest
import  random
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from datetime import date


driver = webdriver.Chrome()
driver.get('https://www.booking.com/')
driver.implicitly_wait(5)


def random_index(end):
    if isinstance(end, int):
        return random.randint(0,end-1)
    else:
        return random.randint(0,len(end)-1)

def get_price_from_list(price_list,list_index):
     price = price_list[list_index].text.split(" ")[1]
     return price


def test_choose_any_city():
    city_tab = driver.find_element_by_xpath("//ul[@role='tablist']/li[contains(text(), 'Cities')]")
    city_tab.click()
    city_list = driver.find_elements_by_xpath("//li[@class='ia_section  active']//a[@class='ia_link']")
    random_city_index = random_index(city_list)
    expected_city = city_list[random_city_index].text.split("\n")[0]
    #print(f'expected city :{city_list[random_city_index].text}')
    city_list[random_city_index].click()
    hotel_header = driver.find_element_by_xpath("//h2[@class='sr-snippet__header']")
    expected_title = f'Hotels and More in {expected_city}'
    #print(f'expected_title:{expected_title}')
    #print(hotel_header.text)
    assert expected_title == hotel_header.text


    # - calendar for specifying check in date is opened
def get_calendar_text():
        calendar_label = driver.find_element_by_class_name('bui-calendar__display')
        #print(f'calendar label:{calendar_label.text}')
        return calendar_label.text


def test_calendar_for_specifying_check_in_is_opened():
    assert get_calendar_text() == 'Check-in - Check-out'


def element_does_not_displayed(xpath):
    if len(driver.find_elements_by_xpath(xpath)):
        return False
    else:
        return True


def is_element_displayed(xpath):
    if len(driver.find_elements_by_xpath(xpath)):
        return True
    else:
        return False


def is_element_displayed_by_class_name(class_name):
    if len(driver.find_elements_by_class_name(class_name)):
        return True
    else:
        return False


def test_no_result_entry_containing_booking_price_():
    booking_prices = '//*[@id="hotellist_inner"]/div[1]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div'
    assert element_does_not_displayed(booking_prices)


def test_no_result_entry_containing_booking_status():
    booking_status= '//*[@id="hotellist_inner"]/div[1]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div[3]/div'
    assert element_does_not_displayed(booking_status)


def go_to_any_hotel_and_click_show_prices():
   lower_price_first = driver.find_element_by_xpath("//div[@class='content__nav']/span[2]")
   lower_price_first.click()
   hotels_list = driver.find_elements_by_xpath("//span[@class='bui-button__text']")
   any_hotel_index = random_index(hotels_list)
   print(hotels_list[any_hotel_index].text)
   hotels_list[any_hotel_index].click()



def test_check_is_calendar_for_specifying_date_is_opened():
    calendar_xpath = "//div[@class='c2-calendar']"
    calendar_class = 'bui-calendar__main b-a11y-calendar-contrasts'
    print(is_element_displayed(calendar_xpath))
    #assert is_element_displayed_by_class_name(calendar_class)

def get_today_date():
    today = date.today()
    return today.strftime("%d")


def set_any_dates():
    #today_date = driver.find_element_by_class_name("bui-calendar__date bui-calendar__date--today")
    today_dateX = driver.find_element_by_xpath(f"//div[contains(@class, 'calendar')]//span[contains(text(), '{get_today_date()}')]")
    print(f'today date {today_dateX.text}')
    today_dateX.click()


def click_submit_button():
    submit_button = driver.find_element_by_class_name("sb-searchbox__button ")
    submit_button.click()

def test_each_result_entry_has_booking_price():
    list_of_prices = driver.find_elements_by_xpath("//div[@class='bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper']")
    prices_list_length = len(list_of_prices[0].text)
    for i in range(0,len(list_of_prices)-1):
        assert len(get_price_from_list(list_of_prices,i)) > 0
        print(get_price_from_list(list_of_prices,i)) ###11111111111111111111


test_choose_any_city()
get_calendar_text()
test_no_result_entry_containing_booking_status()
test_no_result_entry_containing_booking_price_()
go_to_any_hotel_and_click_show_prices()
test_check_is_calendar_for_specifying_date_is_opened()
set_any_dates()
click_submit_button()
test_each_result_entry_has_booking_price()