import allure

from modules.blog_grid import BlogGridPage
from modules.grid_leadership import GridLeadershipPage
from resources.locators import BlogPageLocators

expected_part_text = "director of Grid Dynamics’ board of directors since 2006 and " \
                     "the Chief Executive Officer of Grid Dynamics since 2014"


@allure.description("Test navigate to Blog page with redirecting to About page and checking needed information")
@allure.story("Case 1")
@allure.severity("critical")
def test_verify_info(driver):
    page, page_2 = BlogGridPage(driver), GridLeadershipPage(driver)
    page.open_home_page()
    page.navigation_to_specified_page(hover_need=True,
                                      locator=BlogPageLocators.LEADERSHIP_INNER)
    page_2.navigation_to_head_info()
    page_2.info_about_head_person(expected_part_text)

