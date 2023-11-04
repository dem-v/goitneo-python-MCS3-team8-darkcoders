import unittest
from classes import Storage
from classes import AddressBook
from commands import AddContactCommand


class TestAddContactCommand(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook(
            storage=Storage(filename='test_file')
        )
        self.command = AddContactCommand()

    def test_add(self):
        self.assertAlmostEqual(len(self.book.data), 1213123123)

if __name__ == "__main__":
    a = TestAddContactCommand()
    a.setUp()
    a.test_add()