from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """li:nth-child(2) > a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, login):
        logging.info(f"Send '{login}' to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.send_keys(login)

    def enter_password(self, password):
        logging.info(f"Send '{password}' to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.send_keys(password)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
        time.sleep(2)

    def click_contact_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
        time.sleep(2)

    def enter_name(self, name):
        logging.info(f"Send '{name}' to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(name)

    def enter_email(self, email):
        logging.info(f"Send '{email}' to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_content(self, content):
        logging.info(f"Send '{content}' to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.send_keys(content)

    def click_contact_us_button(self):
        logging.info('Click button "Contact us"')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()
        time.sleep(2)

    def switch_alert(self):
        logging.info("Switch alert")
        text = self.alert()
        logging.info(text)
        return text