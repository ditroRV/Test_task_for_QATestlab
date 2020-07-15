from HomePage import HomePage

def test_user_able_to_specify_age_of_each_child(browser,numberOfChildren):
    number_of_children_to_specify = numberOfChildren
    booking_home_page = HomePage(browser)
    booking_home_page.go_to_site()
    booking_home_page.click_on_stranger_menu()
    booking_home_page.click_children_number_times(number_of_children_to_specify)
    assert booking_home_page.selected_children_ammount() == numberOfChildren






