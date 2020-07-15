from BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators(BasePage):
    LOCATOR_CHILDREN_NUMBER_ELEMENT = (By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/span[1]')
    LOCATOR_ADD_CHILD_BUTTON = (By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[2]')
    LOCATOR_STRANGERS_MENU_SELECTING = (By.XPATH, '//*[@id="xp__guests__toggle"]/span[2]')
    LOCATOR_CHILDREN_SELECTED = (By.CLASS_NAME, 'sb_child_ages_empty_zero')
    LOCATOR_CITY_TAB = (By.XPATH, "//ul[@role='tablist']/li[contains(text(), 'Cities')]")
    LOCATOR_CITY_LIST = (By.XPATH, "//li[@class='ia_section  active']//a[@class='ia_link']")


class HomePage(BasePage):


    def click_children_number_times(self,numberOfChildren=2):

        specified_children_number = int( self.find_element(HomePageLocators.LOCATOR_CHILDREN_NUMBER_ELEMENT).text)

        for _ in range(specified_children_number, numberOfChildren):
            self.find_element(HomePageLocators.LOCATOR_ADD_CHILD_BUTTON).click()


    def click_on_stranger_menu(self):
        return self.find_element(HomePageLocators.LOCATOR_STRANGERS_MENU_SELECTING).click()


    def selected_children_ammount(self):
        return len(self.find_elements(HomePageLocators.LOCATOR_CHILDREN_SELECTED))

    def click_on_city_tab(self):
       return self.find_element(HomePageLocators.LOCATOR_CITY_TAB).click()


    def get_random_city_index(self):
        return BasePage.random_index((self.find_elements(HomePageLocators.LOCATOR_CITY_LIST)))



    def get_expected_city_name(self,random_city_index):
        return self.find_elements(HomePageLocators.LOCATOR_CITY_LIST)[random_city_index].text.split("\n")[0]


    def go_to_city_page(self,city_index):
        city_list =  self.find_elements(HomePageLocators.LOCATOR_CITY_LIST)
        return (city_list[city_index]).click()

    def navigate_to_random_city(self):
        self.click_on_city_tab()
        random_city_index = self.get_random_city_index()
        city = self.get_expected_city_name(random_city_index)
        self.go_to_city_page(random_city_index)
        return city