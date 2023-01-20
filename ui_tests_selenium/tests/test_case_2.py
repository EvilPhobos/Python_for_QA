import allure

from modules.blog_grid import BlogGridPage
from resources.locators import BlogPageLocators


@allure.story("Case 2")
@allure.severity("normal")
def test_verify_articles(driver):
    page = BlogGridPage(driver)
    page.open_home_page()
    page.filter_statuses()
    page.change_filter_value_with_scroll(locator_1=BlogPageLocators.FILTER,
                                         locator_2=BlogPageLocators.FILTER_C_D,
                                         click=True,
                                         scroll=True)
    article_headers = page.search_till_true(search_locator=BlogPageLocators.ART_C_LOCATOR,
                                            base_locator=BlogPageLocators.ARTICLE_CONTAINER,
                                            attr_name="data-postid")
    page.change_filter_value_with_scroll(locator_1=BlogPageLocators.FILTER,
                                         locator_2=BlogPageLocators.FILTER_DEFAULT,
                                         click=True)
    page.search_till_true(search_locator=BlogPageLocators.FIRST_ARTICLE,
                          base_locator=BlogPageLocators.FIRST_ART_LOCATOR,
                          attr_name="data-postid",
                          header_to_compare=article_headers)
