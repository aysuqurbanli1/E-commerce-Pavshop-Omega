import imp
from itertools import product
from math import prod
from unicodedata import category
from django.test import TestCase
from django.urls import reverse_lazy
from product.models import *


class TestProductsAPIView(TestCase):

    @classmethod
    def setUp(cls):
        cls.url=reverse_lazy('api_products')
        category=Category.objects.create(name='one')
        brand=Brand.objects.create(name='brand')
        product=Product.objects.create(brand=brand, category=category)
        cls.valid_data={
            'product': product.id,
            'title':'Product 1',
            'code': 'aaaa',
            'price': 100,
            'stock': 24

        }
        

    def test_api_url(self):
        expected_url='/api/products/'
        print("isledi api")
        self.assertEqual(self.url,expected_url)

    def test_api_post_request_status_code(self):
        res= self.client.post(self.url,data=self.valid_data)
        print(res.json())
        self.assertEqual(res.status_code,201)

    def test_api_post_request_response(self):
        res= self.client.post(self.url,data=self.valid_data)
        result = res.json()
        self.assertEqual(result['title'],self.valid_data['title'])


    def test_api_get_request_status_code(self):
        res= self.client.get(self.url)
        self.assertEqual(res.status_code,200)

    def test_api_get_request_response(self):
        res= self.client.get(self.url)
        print(dir(res))
        self.assertIsInstance(res.json(),list)

    # @classmethod
    # def tearDownClass(cls):
    #     ...
        
