import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual((stock, bid_price, ask_price, price), 
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], expected_price))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual((stock, bid_price, ask_price, price), 
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], expected_price))

    def test_getRatio(self):
        # Test when price_b is not zero
        self.assertEqual(getRatio(120.48, 121.2), 120.48 / 121.2)
        # Test when price_b is zero
        self.assertIsNone(getRatio(120.48, 0))
        # Additional test case where price_a is zero
        self.assertEqual(getRatio(0, 121.2), 0)

if __name__ == '__main__':
    unittest.main()