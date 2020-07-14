from HomePage import HomePage
from CityPage import CityPage
from SearchResults import SearchResults


def test_SecondTestScenario(browser):
    booking_home_page = HomePage(browser)
    city_page = CityPage(browser)
    booking_home_page.go_to_site()
    city = booking_home_page.navigate_to_random_city()
    expected_title = f'Hotels and More in {city}'
    assert expected_title == city_page.get_hotel_header().text
    assert city_page.get_calendar_text() == 'Check-in - Check-out'
    hotels = city_page.hotels_list()
    for hotel in hotels:
        assert 'Avg. price/night' in hotel.text and 'nights' not in hotels
    city_page.click_on_lower_prices_first_tab()
    search_result_page = SearchResults(browser)
    search_result_page.go_to_any_hotel_and_click_show_prices()
    first_calendar = search_result_page.is_element_displayed(search_result_page.get_calendar_xpath())
    second_calendar = search_result_page.is_element_displayed_by_class_name(search_result_page.get_calendar_clas_name())
    assert  first_calendar or second_calendar

    search_result_page.search_any_date()
    prices_list_length = search_result_page.get_prices_list_length()
    prices_list = search_result_page.prices_elements()
    prices = search_result_page.prices()
    for price in prices:
        assert len(price) > 0

