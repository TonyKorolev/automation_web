from testpage import *

with open('testdata.yaml') as f:
    info = yaml.safe_load(f)


def test_create_post():
    post_json = create_post()
    assert post_json['item']['id']


def test_find_post():
    assert info['create_post']['description'] in find_post()


def test_not_my_posts_display(not_my_post):
    assert not_my_post in get_not_my_posts()


def test_my_posts_display():
    assert info['create_post']['content'] in get_my_posts()