import unittest
from listdict import ListDictionary

class TestListDictionary(unittest.TestCase):
    # Define a setup method that will be run before each test method
    def setUp(self):
        # Create an instance of ListDictionary for testing
        self.dict = ListDictionary()

    # Define test methods for each method in ListDictionary

    # Test the insert method
    def test_insert(self):
        # Insert a key-value pair and check if it returns True
        self.assertFalse(self.dict.insert("key_1", 10))
        # Insert another key-value pair with an existing key and check if it returns False
        self.assertTrue(self.dict.insert("key_1", 20))
        # Insert a new key-value pair and check if it returns False
        self.assertFalse(self.dict.insert("key_2", 5))

    # Test the remove method
    def test_remove(self):
        # Insert a key-value pair
        self.dict.insert("key_1", 10)
        # Remove the key-value pair and check if it returns True
        self.assertTrue(self.dict.remove("key_1"))
        # Remove a non-existing key and check if it returns False
        self.assertFalse(self.dict.remove("key_2"))

    # Test the contains method
    def test_contains(self):
        # Insert a key-value pair
        self.dict.insert("key_1", 10)
        # Check if the key exists in the dictionary
        self.assertTrue(self.dict.contains("key_1"))
        # Check if a non-existing key returns False
        self.assertFalse(self.dict.contains("key_2"))

    # Test the lookup method
    def test_lookup(self):
        # Insert a key-value pair
        self.dict.insert("key_1", 10)
        # Check if lookup returns the correct value
        self.assertEqual(self.dict.lookup("key_1"), 10)
        # Check if lookup returns None for a non-existing key
        self.assertIsNone(self.dict.lookup("key_2"))

    # Test the get_keys method
    def test_get_keys(self):
        # Insert multiple key-value pairs
        self.dict.insert("key_1", 10)
        self.dict.insert("key_2", 20)
        # Check if get_keys returns the correct list of keys
        self.assertListEqual(self.dict.get_keys(), ["key_1", "key_2"])

    # Test the get_values method
    def test_get_values(self):
        # Insert multiple key-value pairs
        self.dict.insert("key_1", 10)
        self.dict.insert("key_2", 20)
        # Check if get_values returns the correct list of values
        self.assertListEqual(self.dict.get_values(), [10, 20])

    # Test the size method
    def test_size(self):
        # Insert multiple key-value pairs
        self.dict.insert("key_1", 10)
        self.dict.insert("key_2", 20)
        # Check if size returns the correct number of key-value pairs
        self.assertEqual(self.dict.size(), 2)
    
    # def test_insert(self):
    #     ldict = ListDictionary()
    #     # insert() should return false if not
    #     # overwriting a key
    #     assert not ldict.insert(1, "hello")

    # add more unit tests below
