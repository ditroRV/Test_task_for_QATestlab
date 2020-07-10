import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.booking.com/')
ChildrenNumberElement = driver.find_element_by_xpath('//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/span[1]')

@pytest.fixture()
def numberOfChildren():
    numberOfChildren = 2
    return numberOfChildren


def validate_number_of_children_more_than_one(numberOfChildren):
    print(numberOfChildren)
    if numberOfChildren > 1:
        return True
    else:
        return False


def ChildrenNumber(numberOfChildren):
    add_child_button = driver.find_element_by_xpath('//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[2]')
    specified_children_number = int(ChildrenNumberElement.text)

    if validate_number_of_children_more_than_one:
        for _ in range(specified_children_number,numberOfChildren):
            add_child_button.click()
    else:
        return 'erorr'



def test_user_able_to_specify_age_of_each_child(numberOfChildren):
    strangersMenuSelecting = driver.find_element_by_xpath('//*[@id="xp__guests__toggle"]/span[2]')
    strangersMenuSelecting.click()
    all_children_by_xpath = driver.find_elements_by_class_name('sb-group__children__field clearfix')
    ChildrenNumber(numberOfChildren)
    children_selects = driver.find_elements_by_class_name('sb_child_ages_empty_zero')
    print(f'number of childrens selects: {len(children_selects)}')
    print('numberOfChildrenZadano',numberOfChildren)
    assert len(children_selects) == numberOfChildren







