import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from todo import TodoApp

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.app = TodoApp()

    def test_add_todo(self):
        self.app.add_todo("Buy milk")
        self.assertEqual(len(self.app.todos), 1)
        self.assertEqual(self.app.todos[0].title, "Buy milk")
        self.assertFalse(self.app.todos[0].completed)

    def test_complete_todo(self):
        self.app.add_todo("Buy milk")
        result = self.app.complete_todo(0)
        self.assertTrue(result)
        self.assertTrue(self.app.todos[0].completed)

    def test_remove_todo(self):
        self.app.add_todo("Buy milk")
        result = self.app.remove_todo(0)
        self.assertTrue(result)
        self.assertEqual(len(self.app.todos), 0)

    def test_list_todos(self):
        self.app.add_todo("Buy milk")
        self.app.add_todo("Read book")
        todos = self.app.list_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[1].title, "Read book")

if __name__ == "__main__":
    unittest.main()
