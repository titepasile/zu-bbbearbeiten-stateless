import unittest
import helper

class TestMethod1(unittest.TestCase):
    def test_add(self):
        str = "Item"
        helper.add("Item")
        self.assertEqual(helper.todos[-1].title, str)

    def test_update(self):
        helper.todos.append(helper.todo("Item"))
        helper.update(0)
        self.assertTrue(helper.todos[0].isCompleted)

