import allure
from resources.page import Base
from resources.locators import BlogPageLocators
from modules.specific_func import list_exclude_xpath_creation


class BlogGridPage(Base):
    @allure.step("Step 1: Open page")
    def open_home_page(self):
        """Navigation to start page"""
        self.navigate(BlogPageLocators.URL_START_PAGE)

    @allure.step("Step 2: Navigation to [specified] page")
    def navigation_to_specified_page(self, locator: str, time: int = 5,
                                     hover_need: bool = None):
        """ Click action on [specified] web element with optional function "hover" before action

        :param locator: locator with type for element which need to click
        :param time: timeout for action, default 5 sec
        :param hover_need: if need hover the element before click
        """
        if hover_need:
            self.hover_element(BlogPageLocators.ABOUT_DROPDOWN)
        self.click(self.wait_until_elem_located(time, locator))

    @allure.step("Step 2: check ‘filter’ visible and available")
    def filter_statuses(self):
        """Check ‘filter’ visible and available statuses"""
        element = self.find_the_element(BlogPageLocators.FILTER)
        available = self.availability_status(element)
        visible = self.visibility_status(element)
        assert available and visible, f'Filter display or availability status not correct:\n' \
                                      f'Actual: availability = available, visibility = {visible}\n' \
                                      f'Expected: True'

    @allure.step("Step: Open ‘filter’ list and set needed topic")
    def change_filter_value_with_scroll(self, locator_2: str, locator_1: str = None,
                                        click: bool = False, scroll: bool = False):
        """Apply filter and return article count

        :param locator_1: locator for scroll
        :param locator_2: locator for click
        :param click: if need to click locator_1 element
        :param scroll: if need to scroll to locator_1 element
        """
        if scroll or click:
            element = self.find_the_element(locator_1)
        if scroll:
            self.scroll_to_element(element, -115)
            self.pause(0.5)
        if click:
            self.click(element)

        self.click(self.find_the_element(locator_2))

    @allure.step("Step: Check there is more than 1 article in [selected] topic")
    def search_till_true(self, search_locator: str, base_locator: str,
                         attr_name: str, header_to_compare: list = None) -> list:
        """Search in loop for each element that match locator

        :param search_locator: param with type for search
        :param base_locator: locator to find elements list
        :param attr_name: name of attribute to specify each f.e. id or class or...
        :param header_to_compare: if specified, will be compared with current headers
        :return: headers list
        """
        status = True
        locator_list = []
        header_list = []
        while status:
            status = self.search_status(search_locator)
            if status:
                locator_list.append(self.find_the_element(search_locator).get_attribute(attr_name))
                header_list.append(str(self.find_the_element(search_locator).text))
                search_locator_c = list(search_locator)
                search_locator_c[1] = list_exclude_xpath_creation(base_locator[1], attr_name, locator_list)
                search_locator = tuple(search_locator_c)

        assert len(locator_list) > 1, f'Article amount less than needed:\n' \
                                      f'Actual: {len(locator_list)}\n' \
                                      f'Expected: > 1'
        if header_to_compare:
            assert header_list[1] not in header_to_compare[1], f'Article headers equal:\n' \
                                                               f'Actual: {header_to_compare[1]} == {header_list[1]}\n' \
                                                               f'Expected: {header_to_compare[1]} != {header_list[1]}'
        return header_list
