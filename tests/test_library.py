import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    """Test library to test for some functions in Library class."""

    def setUp(self):
        """Set up the Library instance for testing"""
        self.library = Library("data/books.txt")
        self.library._books = {
            "The journey": {
                "author": "Michael john",
                "year": 2021,
                "available": True
            },
            "Enjoy your life": {
                "author": "Maher Zaid",
                "year": 2012,
                "available": True
            }
        }
    def test_borrow_books(self):
        """Test that the Library instance is correctly working"""
        self.library.borrow_book("The journey", "User1")
        self.assertFalse(
            self.library._books["The journey"]["available"])

    def test_return_books(self):
        """Test that the Library instance is correctly working"""
        self.library.borrow_book("The journey", "User1")
        self.library.return_book("The journey", "User1")
        self.assertTrue(
            self.library._books["The journey"]["available"]
        )


if __name__ == "__main__":
    unittest.main()
