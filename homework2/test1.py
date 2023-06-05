import yaml
from module import Site
import pytest
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


@pytest.mark.skip
def test_checking_error(x_selector1, x_selector2, x_selector3, btn_selector, result):

    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

    btn = site.find_element("css", btn_selector)
    btn.click()

    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == result

    site.close()


@pytest.mark.skip
def test_successful_authotization(x_selector1, x_selector2, btn_selector, hello_user):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata['passwd'])

    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(3)
    element = site.find_element("xpath", hello_user)
    assert element.text == f"Hello, {testdata['login']}"

    site.close()


# Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
# Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.


def test_creating_post(x_selector1, x_selector2, btn_selector, btn_create_post, post_title, post_description, 
                       post_content, btn_save_post, post_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(testdata['login'])

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(testdata['passwd'])

    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(2)

    btn_create_posts = site.find_element("css", btn_create_post)
    btn_create_posts.click()

    title = site.find_element("xpath", post_title)
    title.send_keys(testdata['title'])

    description = site.find_element("xpath", post_description)
    description.send_keys(testdata['description'])

    content = site.find_element("xpath", post_content)
    content.send_keys(testdata['content'])

    btn_save_posts = site.find_element("css", btn_save_post)
    btn_save_posts.click()

    time.sleep(2)
    check_post = site.find_element("xpath", post_name)
    assert check_post.text == f"{testdata['title']}"

    site.close()