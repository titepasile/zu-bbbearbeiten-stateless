import unittest
import helper

class TestHelperFunctions(unittest.TestCase):

    def test_bbb(self):
        helper.add("b")
        self.assertEqual(helper.todos[-1].title, "bbb")

    def test_Bbb(self):
        helper.add("B")
        self.assertEqual(helper.todos[-1].title, "Bbb")

    def test_Bbb_in_word(self):
        helper.add("Baden")
        self.assertEqual(helper.todos[-1].title, "Bbbaden")