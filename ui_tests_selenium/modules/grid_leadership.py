import allure
from resources.page import Base
from resources.locators import LeadershipPageLocators


class GridLeadershipPage(Base):
    @allure.step("Step 3: Find Leonard Livschitz and click on the name")
    def navigation_to_head_info(self):
        self.banner_closing(LeadershipPageLocators.BANNER_CONTAINER)
        self.click(self.find_the_element(LeadershipPageLocators.HEAD_PERSON))

    @allure.step("Step 4: Verify that information about Leonard has appeared and the text...")
    def info_about_head_person(self, expected_part_text):
        """ Verify the information from text web element
        :param expected_part_text: text to compare with
        """
        actual_d_status = self.visibility_status(self.find_the_element(LeadershipPageLocators.TEXT_CONTAINER))
        actual_full_text = self.text_return(self.find_the_element(LeadershipPageLocators.TEXT_CONTAINER))

        assert expected_part_text in actual_full_text, f'Searched text not found:\n' \
                                                       f'Actual: {actual_full_text}\n' \
                                                       f'Expected: {expected_part_text}'
        assert actual_d_status, f'Text display status not correct:\n' \
                                f'Actual: {actual_d_status}\n' \
                                f'Expected: True'
