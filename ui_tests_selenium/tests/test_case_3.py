import allure

from ui_tests_selenium.modules.blog_grid import BlogGridPage
from ui_tests_selenium.modules.grid_contact import GridContactPage
from ui_tests_selenium.resources.locators import BlogPageLocators, ContactPageLocators


"""Case #3:
+ Open https://blog.griddynamics.com
+ Click on Get In Touch button
+ Ensure page Contact Us opened

Fill in the following:
- First Name = Anna, Last Name = Smith
- email = annasmith@griddynamics.com
- select  How did you hear about us? = Online Ads
- Click on checkbox “I have read and accepted the Terms & Conditions and Privacy Policy”
- Click on checkbox “I allow Grid Dynamics to contact me”

Ensure Contact button is inactive"""

first_name = "Anna"
last_name = "Smith"
email = "annasmith@griddynamics.com"
hear_about_us = "Online Ads"
check_box_text_1 = "I have read and accepted the"
check_box_text_2 = "I allow Grid Dynamics to contact me"


@allure.story("Case 3")
@allure.severity("blocker")
def test_verify_articles(driver):
    blog_page, contact_page = BlogGridPage(driver), GridContactPage(driver)
    blog_page.open_home_page()
    blog_page.navigation_to_specified_page(locator=BlogPageLocators.GET_IN_TOUCH)
    contact_page.ensure_need_page_open(ContactPageLocators.URL)
    contact_page.fill_contact_form(first_name=first_name,
                                   last_name=last_name,
                                   mail=email,
                                   hear_about_opt=hear_about_us,
                                   check_box_text_1=check_box_text_1,
                                   check_box_text_2=check_box_text_2)

    contact_page.check_button_status()
