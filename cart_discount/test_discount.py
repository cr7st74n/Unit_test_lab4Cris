import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))


    def Test_list_of_two_prices_no_discount(self):
        prices = [21,3]
        except_discount = 0
        actual_discount = discount(prices)
        self.assertEqual(except_discount, actual_discount)
    

    def test_list_of_several_items_with_same_price(self):
        prices = [21,3,45,5,34,23,655,6,3]
        except_discount = 3
        actual_discount = discount(prices)
        self.assertEqual(except_discount, actual_discount)
    
    def test_list_of_no_items(self):
        prices = []
        except_discount = 0
        actual_discount = discount(prices)
        print(actual_discount)
        self.assertEqual(except_discount, actual_discount)
        
        
        # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()