from binary_search import BinarySearch
import unittest
import json
import time
import os

bs = BinarySearch()
file_path = os.path.join(os.getcwd(), 'Capítulo 1', 'items.json')

with open(file_path, "r") as file:
  data = json.load(file)

simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]

class TestBinarySearch(unittest.TestCase):

  def setUp(self):
    print (".......... %s" % self._testMethodName)

  def test_iterative_binary_search_with_simple_list(self):
    item, expected_index = 3, 1
    index = bs.search_iterative(simple_list, item) # => 1
    self.assertEqual(expected_index, index)

  def test_recoursive_binary_search_with_simple_list(self):
    item, expected_index = 3, 1
    low, high = 0, len(simple_list) - 1
    index = bs.search_recursive(simple_list, low, high, item)
    self.assertEqual(expected_index, index)

  def test_search_for_nonexistent_item(self):
    item, expected_result = 100, None
    index = bs.search_iterative(simple_list, item)
    self.assertEqual(expected_result, index)

  def test_binary_search_and_linear_search_execution_time(self):
    item, expected_index = 9887, 990
    start_time = time.time()
    binary_search_index = bs.search_iterative(list_with_1000_items, item)
    bs_time = time.time() - start_time
    start_time = time.time()
    linear_search_index = list_with_1000_items.index(item)
    ls_time = time.time() - start_time
    self.assertEqual(expected_index, binary_search_index)
    self.assertEqual(expected_index, linear_search_index)
    self.assertTrue(bs_time < ls_time)

  def test_execution_time_for_item_at_the_beginning(self):
    item, expected_index = 55, 10
    start_time = time.time()
    binary_search_index = bs.search_iterative(list_with_1000_items, item)
    bs_time = time.time() - start_time
    start_time = time.time()
    linear_search_index = list_with_1000_items.index(item)
    ls_time = time.time() - start_time
    self.assertEqual(expected_index, binary_search_index)
    self.assertEqual(expected_index, linear_search_index)
    self.assertTrue(bs_time > ls_time)

if __name__ == '__main__':
    unittest.main()