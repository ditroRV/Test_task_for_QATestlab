from HomePage import HomePage
from CityPage import CityPage
from SearchResults import SearchResults


def test_SecondTestScenario(browser):

    booking_home_page = HomePage(browser)

    city_page = CityPage(browser)
    booking_home_page.go_to_site()
    city = booking_home_page.navigate_to_random_city()
    assert city_page.is_page_title_corect(city)
    assert city_page.is_calendar_open_for_specifying()
    assert  city_page.is_no_result_entry_containing_booking_price_or_booking_status()
    city_page.click_on_lower_prices_first_tab()
    search_result_page = SearchResults(browser)
    search_result_page.go_to_any_hotel_and_click_show_prices()
    assert  search_result_page.is_calendars_displayed()
    search_result_page.set_date_and_click_submit_button()
    assert search_result_page.is_price_displayed()
