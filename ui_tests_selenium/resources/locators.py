from selenium.webdriver.common.by import By


class BlogPageLocators:
    URL_START_PAGE = 'https://blog.griddynamics.com'
    ABOUT_DROPDOWN = (By.XPATH, '//a[contains(text(),"About")]')
    LEADERSHIP_INNER = (By.XPATH, '//a[contains(text(),"Leadership")]')
    FILTER = (By.XPATH, '//div[@id = "topiclist"]/div')
    FILTER_DEFAULT = (By.XPATH, '//span[text()="All topics"]')
    FILTER_C_D = (By.XPATH, '//span[text()="Cloud and DevOps"]')
    ARTICLE_CONTAINER = (By.XPATH, '//*[contains(@class,"cloud-and")]//a[(@class = "card cardtocheck")]')
    ART_C_LOCATOR = (By.XPATH, ARTICLE_CONTAINER[1] + '[not(@data-postid="")]')
    FIRST_ARTICLE = (By.XPATH, '//div[@class = "row first"]/..//a[@class="card cardtocheck"]')
    FIRST_ART_LOCATOR = (By.XPATH, FIRST_ARTICLE[1] + '[not(@data-postid="")]')
    GET_IN_TOUCH = (By.XPATH, '//div[contains(@class,"gd-container")]/*[@gdbutton]')


class LeadershipPageLocators:
    BANNER_CONTAINER = (By.XPATH,
                        '//div[contains(@class, "banner-container")]//button[contains(@class, "close-button")]')
    HEAD_PERSON = (By.XPATH, '//button[@class="person-head"]//div[contains(text(),"Leonard Livschitz")]')
    TEXT_CONTAINER = (By.XPATH, '//div[@dir="ltr"]//gd-wysiwyg-content')


class ContactPageLocators:
    URL = 'https://www.griddynamics.com/contact'
    FIRST_NAME = (By.XPATH, '//input[@formcontrolname = "firstName"]')
    LAST_NAME = (By.XPATH, '//input[@formcontrolname = "lastName"]')
    E_MAIL = (By.XPATH, '//input[@formcontrolname = "email"]')
    HEAR_ABOUT = (By.XPATH, '//*[@formcontrolname = "source"]')
    HEAR_ABOUT_INNER = (By.XPATH, '//gd-select-option[contains(text(), "%s" )]')
    CONDITION_SEARCH = (By.XPATH, '//*[contains(text(), "%s")]/..//div[@class = "ui-checkbox-cell"]')  # %"some specified text"
    SUBMIT_BUTTON = (By.XPATH, '//*[contains(@class, "submit-button")]')
