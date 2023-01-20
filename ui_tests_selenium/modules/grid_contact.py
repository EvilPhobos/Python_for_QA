import allure

from ui_tests_selenium.resources.page import Base
from ui_tests_selenium.resources.locators import ContactPageLocators
from ui_tests_selenium.modules.specific_func import tuple_update


class GridContactPage(Base):
    @allure.step("Step 3: Ensure page Contact Us opened")
    def ensure_need_page_open(self, expected_url: str):
        """ Compare current page with expected
        :param expected_url: url with which to compare
        """
        actual_url = self.current_url()
        assert actual_url == expected_url, f'URL not correct:\n' \
                                           f'Actual: {actual_url}\n' \
                                           f'Expected: {expected_url}]'

    @allure.step("Step 4: Fill in the form")
    def fill_contact_form(self, first_name, last_name, mail, hear_about_opt, check_box_text_1, check_box_text_2):
        """
        :param first_name: value to insert into first name cell
        :param last_name: value to insert into last name cell
        :param mail: value to insert into e-mail cell
        :param hear_about_opt: value to chose from "How did you hear about us?" form
        :param check_box_text_1: set checkbox #1
        :param check_box_text_2: set checkbox #2
        """
        # set the value to the fields
        self.set_input_value(ContactPageLocators.FIRST_NAME, first_name)
        self.set_input_value(ContactPageLocators.LAST_NAME, last_name)
        self.set_input_value(ContactPageLocators.E_MAIL, mail)

        # select value from dropdown
        self.click(self.find_the_element(ContactPageLocators.HEAR_ABOUT))
        self.click(self.find_the_element(tuple_update(1, ContactPageLocators.HEAR_ABOUT_INNER, hear_about_opt)))

        # scroll to next elements
        scroll_element = self.find_the_element(tuple_update(1, ContactPageLocators.CONDITION_SEARCH, check_box_text_1))
        self.scroll_to_element(scroll_element, -135)
        self.pause(0.5)

        # set checkboxes
        self.click(scroll_element)
        self.click(self.find_the_element(tuple_update(1, ContactPageLocators.CONDITION_SEARCH, check_box_text_2)))

    @allure.step("Step 5: Ensure Contact button is inactive")
    def check_button_status(self):
        """Check button status"""
        button_status = self.availability_status(self.find_the_element(ContactPageLocators.SUBMIT_BUTTON))
        assert not button_status, f'Text display status not correct:\n' \
                                  f'Actual: {button_status}\n' \
                                  f'Expected: False'
