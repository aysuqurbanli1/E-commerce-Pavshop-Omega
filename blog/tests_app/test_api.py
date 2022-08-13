import imp
from itertools import product
from math import prod
from unicodedata import category
from django.test import TestCase
from django.urls import reverse_lazy
from product.models import *


class TestBlogsAPIView(TestCase):

    @classmethod
    def setUp(cls):
        cls.url=reverse_lazy('api_blogs')
        print(cls.url)


    def test_api_url(self):
        expected_url='/api/blogs/'
        print("isledi api blog -------------")
        self.assertEqual('/api/blogs/',expected_url)


    # @classmethod
    # def tearDownClass(cls):
    #     ...
    