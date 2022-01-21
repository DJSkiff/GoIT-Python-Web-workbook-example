import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        print("Setup code. Lets create a new db mock if there is no")
        if not hasattr(self, "db"):
            self.db = {}

    def tearDown(self):
        print("Clear after test")
        self.db.clear()

    def test_db_update(self):
        new_row = {'a': 1}
        self.db.update(new_row)
        self.assertEqual(self.db, new_row)


    def test_db_pop(self):
        new_row = {'a': 1}
        self.db.update(new_row)
        popped_row = self.db.pop('a')
        self.assertEqual(popped_row, new_row['a'])


if __name__ == '__main__':
    unittest.main()