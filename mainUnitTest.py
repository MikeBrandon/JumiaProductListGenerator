import unittest
from selenium import webdriver
import page
import strings


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(strings.CHROME_DRIVER_PATH)
        self.driver.get(strings.JUMIA_HOMEPAGE)

    def test_search_jumia(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "jacket"
        main_page.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
