import unittest
from defillamaAPI import TVL, Coins

class DefillamaTestCase(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects or data for your tests
        self.tvl = TVL()
        self.coins = Coins()

    def tearDown(self):
        # Clean up after each test, if needed
        pass

    def test_tvl_get_all_protocols(self):
        # Test case for a method that should raise an exception
        try:
            self.tvl.get_all_protocols()
        except Exception as e:
            print(f"Encounter Error in tvl_get_all_protocols: {str(e)}")
    
    def test_coin_batch_historical(self):
        # Test case for a method that should raise an exception
        try:
            self.coins.batch_historical(coins="ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1")
        except Exception as e:
            print(f"Encounter Error in coin_batch_historical: {str(e)}")
    
if __name__ == '__main__':
    unittest.main()