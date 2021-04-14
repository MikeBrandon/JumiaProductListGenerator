import strings
from locators import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return strings.JUMIA_TITLE in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    def is_result_found(self):
        return "There are no results for " not in self.driver.page_source