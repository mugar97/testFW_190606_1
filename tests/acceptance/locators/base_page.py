from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'
    NAV_LINKS = By.TAG_NAME, 'a'
