import imp
from itertools import product
from math import prod
from unicodedata import category
from django.test import TestCase
from django.urls import reverse_lazy
from account.models import *


class TestProductsAPIView(TestCase):

    @classmethod
    def setUp(cls):
        cls.url=reverse_lazy('auth_register')
        cls.valid_data={
            'first_name': 'Name',
            'last_name':'lastname 1',
            'username': 'admin',
            'email': 'email@gmail.com',
            'phone': '123456787654',
            'password':'asdfghjkuyt12345',
            'confirm_password':'asdfghjkuyt12345',
            'address':'address',
            'town_city':'city',
            'country':'Az'

        }



    def test_api_url(self):
        expected_url='/api/account/register/'
        print("isledi api account----------__")
        self.assertEqual(self.url,expected_url)


    def test_api_post_request_status_code(self):
        res= self.client.post(self.url,data=self.valid_data)
        print(res.json())
        self.assertEqual(res.status_code,201)

    def test_api_post_request_response(self):
        res= self.client.post(self.url,data=self.valid_data)
        result = res.json()
        print('account register')
        self.assertEqual(result['username'],self.valid_data['username'])


   