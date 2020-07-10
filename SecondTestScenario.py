import pytest
import  random
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.booking.com/')


def test_choose_any_city():
    city_tab = driver.find_element_by_xpath("//ul[@role='tablist']/li[contains(text(), 'Cities')]")
    city_tab.click()
    city_list = driver.find_elements_by_xpath("//li[@class='ia_section  active']//a[@class='ia_link']")
    random_city_index = random.randint(1, len(city_list))
    expected_city = city_list[random_city_index].text.split("\n")[0]
    print(f'expected city :{city_list[random_city_index].text}')
    city_list[random_city_index].click()
    time.sleep(2)
    hotel_header = driver.find_element_by_xpath("//h2[@class='sr-snippet__header']")
    print(hotel_header.text)
    expected_title = f'Hotels and More in {expected_city}'
    print(f'expected_title:{expected_title}')
    print(hotel_header.text)
    assert expected_title == hotel_header.text



#test_choose_any_city()