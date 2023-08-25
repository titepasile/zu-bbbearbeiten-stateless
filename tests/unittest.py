import unittest
import helper

class TestMethod1(unittest.TestCase):
    def test_replace1(self):
        self.assertEqual('b'.replace(), 'BBB')

    def test_check(self):
        self.assertTrue('BBB'.isupper())
        self.assertFalse('b'.isupper())

    def test_final(self):
        b = 'baden'
        self.assertEqual(b.bbb(), ['b', 'BBB'])
        with self.assertRaises(TypeError):
            b.bbb("BBB")
    
    if "b" == "BBB":
        unittest.main()