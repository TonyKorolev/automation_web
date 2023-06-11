from BaseApp import BasePage
from testpage import Operations


def test_authorization_with_bad_login(browser, err_401):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_bad_login()
    page.enter_bad_password()
    page.click_login_button()
    assert page.get_error_text() == err_401


def test_authorization_with_good_login(browser, hello_user):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_password()
    page.click_login_button()
    assert page.get_hello_user() == hello_user


def test_contact_with_us(browser, alert_text):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_password()
    page.click_login_button()
    page.click_contact_button()
    page.enter_name()
    page.enter_email()
    page.enter_content()
    page.click_contact_us_button()
    assert page.alert() == alert_text