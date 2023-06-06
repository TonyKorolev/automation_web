from testpage import OperationsHelper as OH
import logging
import yaml


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    login = testdata["login"]
    password = testdata["password"]


def test_contact_us(browser):
    logging.info('Test Starting')
    testpage = OH(browser)
    testpage.go_to_site()
    testpage.enter_login(login)
    testpage.enter_password(password)
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name('Tony Corleone')
    testpage.enter_email('antoshka.992@mail.ru')
    testpage.enter_content("WTF! Your site have a lot of bugs! It is very ugly! Do you have good QA engineers to test your site?")
    testpage.click_contact_us_button()
    assert testpage.alert() == 'Form successfully submitted'