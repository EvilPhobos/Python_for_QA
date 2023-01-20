from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Base:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Action: Navigation")
    def navigate(self, url_link: str):
        self.driver.get(url_link)

    @allure.step("Action: Perform")
    def perform(self, web_obj: object):
        """Apply some action done under web element

        :param web_obj: web element object
        """
        return web_obj.perform()

    @allure.step("Action: Click")
    def click(self, web_obj):
        """Perform click action on web element

        :param web_obj: web element object
        """
        return web_obj.click()

    @allure.step("Action: Find the element")
    def find_the_element(self, locator):
        """Find the element

        :param locator: locator with type of the element
        :return: action on web element object
        """
        return self.driver.find_element(locator[0], locator[1])

    @allure.step("Action: Return text attribute from web element")
    def text_return(self, web_obj) -> str:
        """Return text attribute from web element

        :param web_obj: web element object
        :return: text attribute
        """
        return web_obj.text

    @allure.step("Action: Return current page URL")
    def current_url(self) -> str:
        """Return current page URL

        :return: current page URL
        """
        return self.driver.current_url

    @allure.step("Action: Return current web element displaying status")
    def visibility_status(self, web_obj) -> bool:
        """Return current web element displaying status

        :param web_obj: web element object
        :return: web element object status
        """
        return web_obj.is_displayed()

    @allure.step("Action: Return current web element enabling status")
    def availability_status(self, web_obj) -> bool:
        """Return current web element enabling status

        :param web_obj: web element object
        :return: web element object status
        """
        return web_obj.is_enabled()

    @allure.step("Action: Creation presence_of_element_located object")
    def method_object_creation(self, locator):
        """Creation presence_of_element_located object

        :param locator: locator with type of the element
        """
        return EC.presence_of_element_located((locator[0], locator[1]))

    @allure.step("Action: Set value into web element `input`")
    def set_input_value(self, locator, input_value):
        """Set value into "input" web element

        :param locator: locator with type of the element
        :param input_value: what text need to enter to the field
        """
        return self.find_the_element(locator).send_keys(input_value)

    @allure.step("Action: Wait until element located")
    def wait_until_elem_located(self, time, locator):
        """Wait until element located

        :param time: timeout
        :param locator: locator with type of the element
        """
        return WebDriverWait(self.driver, time).until(self.method_object_creation(locator))

    @allure.step("Action: Get web element attribute value")
    def get_attribute_value(self, attr_name: str, search_locator: str) -> str:
        """Get web element attribute value (f.e. class, id or...)

        :param attr_name: name of attribute
        :param search_locator: locator with type of the element
        :return: attribute value
        """
        return str(self.find_the_element(search_locator).get_attribute(attr_name))

    @allure.step("Action: Scroll to elem by amount")
    def scroll_to_element(self, web_obj, correction: int):
        """ Scroll to elem by amount

        :param web_obj: element to which need to scroll
        :param correction: Some amount to scroll more or less
        :return: action, scroll to element
        """
        return ActionChains(self.driver).scroll_by_amount(0, web_obj.location['y'] + correction).perform()

    @allure.step("Action: Wait until some action will be done")
    def wait_until(self, action):
        """Wait until some action will be done

        :param action: completed action object with element
        """
        return WebDriverWait(self.driver, 5).until(action)

    @allure.step("Action: Pause all actions")
    def pause(self, amount: int or float):
        """Pause all actions

        :param amount: time in sec
        :return:
        """
        return ActionChains(self.driver).pause(amount).perform()

    @allure.step("Action: Hover the web element")
    def hover_element(self, locator):
        """Hover the web element

        :param locator: locator with type of the element
        """
        item = self.find_the_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(item).perform()

    @allure.step("Action: Close the banner")
    def banner_closing(self, locator):
        """Close the banner, without fail

        :param locator: locator with type of the element
        """
        try:
            self.click(self.find_the_element(locator))
        finally:
            return

    @allure.step("Action: Try to find some web element and return status of this action")
    def search_status(self, locator) -> bool:
        """Try to find some web element and return status of this action

        :param locator: locator with type of the element
        :return: status
        """
        try:
            elem = self.find_the_element(locator)
        except:
            return False
        else:
            return True
