import re
import unittest
import json

url_file = open('new_user_info.json', 'r', encoding='utf-8')
data = json.load(url_file)


class MyTestCase(unittest.TestCase):
    def test_type_name(self):
        self.assertEqual(data['data']['user']['result']['__typename'], 'User')

    def test_size_id(self):
        self.assertEqual(len(data['data']['user']['result']['id']), 32)

    def test_number_rest_id(self):
        self.assertRegex(data['data']['user']['result']['rest_id'], r'^[0-9]+')

    def test_none_name(self):
        self.assertIsNotNone(data['data']['user']['result']['legacy']['name'])

    def test_none_screen_name(self):
        self.assertIsNotNone(data['data']['user']['result']['legacy']['screen_name'])

    def test_int_fast_followers_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['fast_followers_count']), int)

    def test_int_favourites_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['favourites_count']), int)

    def test_int_followers_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['followers_count']), int)

    def test_int_friends_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['friends_count']), int)

    def test_int_listed_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['listed_count']), int)

    def test_int_media_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['media_count']), int)

    def test_int_normal_followers_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['normal_followers_count']), int)

    def test_int_statuses_count(self):
        self.assertIs(type(data['data']['user']['result']['legacy']['statuses_count']), int)


if __name__ == '__main__':
    unittest.main()
