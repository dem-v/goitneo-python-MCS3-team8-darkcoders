import unittest
from BlackBook import Storage
from BlackBook import AddressBook
from BlackBook import AddContactCommand


class TestAddCommand(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook(
            storage=Storage(filename='test_file')
        )
        self.command = AddContactCommand()

    def test_add(self):
        self.assertAlmostEqual(len(self.book.data), 1213123123)
