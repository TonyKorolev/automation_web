from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import requests
import time


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class TestLocators:
    locs = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for i in locators['xpath'].keys():
        locs[i] = (By.XPATH, locators['xpath'][i])

    for i in locators['css'].keys():
        locs[i] = (By.CSS_SELECTOR, locators['css'][i])


class Operations(BasePage, TestLocators):

# ENTER TEXT
    
    def enter_bad_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.locs['login'])
        if input1:
            input1.send_keys(testdata['bad_username'])
        else:
            logging.error('Enter login field is not found')

    def enter_bad_password(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.locs['password'])
        if input2:
            input2.send_keys(testdata['bad_username'])
        else:
            logging.error('Enter password field is not found')

    def enter_good_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.locs['login'])
        if input1:
            input1.send_keys(testdata['username'])
        else:
            logging.error('Enter login field is not found')

    def enter_good_password(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.locs['password'])
        if input2:
            input2.send_keys(testdata['password'])
        else:
            logging.error('Enter password field is not found')

    def enter_name(self):
        logging.info('Enter name ')
        name_field = self.find_element(self.locs['name_field'])
        if name_field:
            name_field.send_keys(testdata['contact_us']['name'])
        else:
            logging.error('Enter name field is not found')

    def enter_email(self):
        logging.info('Enter email ')
        email_field = self.find_element(self.locs['email_field'])
        if email_field:
            email_field.send_keys(testdata['contact_us']['email'])
        else:
            logging.error('Enter email field is not found')

    def enter_content(self):
        logging.info('Enter content ')
        content_field = self.find_element(self.locs['content_field'])
        if content_field:
            content_field.send_keys(testdata['contact_us']['content'])
        else:
            logging.error('Enter email field is not found')

# CLICK

    def click_login_button(self):
        logging.info('Click login button ')
        btn = self.find_element(self.locs['btn_selector'])
        if btn:
            btn.click()
            time.sleep(3)
        else:
            logging.error('Login button is not found')

    def click_contact_button(self):
        logging.info('Click contact button ')
        cont_btn = self.find_element(self.locs['contact_btn'])
        if cont_btn:
            cont_btn.click()
            time.sleep(3)
        else:
            logging.error('Conctact button is not found')

    def click_contact_us_button(self):
        logging.info('Click contact us button ')
        cont_us_btn = self.find_element(self.locs['contact_us_btn'])
        if cont_us_btn:
            cont_us_btn.click()
            time.sleep(3)
        else:
            logging.error('Contact us button is not found')

# GET TEXT

    def get_error_text(self):
        err_label = self.find_element(self.locs['err_label'])
        if err_label:
            text = err_label.text
            logging.info(f'Error {text} while loging')
            return text
        else:
            logging.error(f'Element with error {text} is not found')
            return None

    def get_hello_user(self):
        hello = self.find_element(self.locs['hello_user'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('"Hello, User" element is not found')
            return None

    def switch_alert(self):
        logging.info('Switch alert')
        text = self.alert()
        logging.info(text)
        return text


def get_token():
    r = requests.post(testdata['getaway']['login'], data={'username': testdata['username'], 'password': testdata['password']})
    return r.json()['token']

def get_my_posts():
    logging.info('Get list with my posts')
    g = requests.get(testdata['api']['posts'],
                    headers={'X-Auth-Token': get_token()})
    if g:
        listcont = [i['content'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('List with my posts is not recieved')


def get_not_my_posts():
    logging.info('Get list with not my posts')
    g = requests.get(testdata['api']['posts'], headers={'X-Auth-Token': get_token()},
                    params={'owner': 'notMe'})
    if g:
        listcont = [i['content'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('List with not my posts is not recieved')


def create_post():
    logging.info('Create new post')
    p = requests.post(testdata['getaway']['posts'], headers={'X-Auth-Token': get_token()},
                    data={'title': testdata['create_post']['title'],
                            'description': testdata['create_post']['description'],
                            'content': testdata['create_post']['content']})
    if p:
        return p.json()
    else:
        logging.error('Post is not created')


def find_post():
    logging.info('Find created post')
    d = requests.get(testdata['api']['posts'], headers={'X-Auth-Token': get_token()})
    if d:
        listdescript = [i['description'] for i in d.json()['data']]
        return listdescript
    else:
        logging.error('Post is not found')