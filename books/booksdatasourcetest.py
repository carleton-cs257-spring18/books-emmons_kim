#hi

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.source_checker = booksdatasource.BooksDataSource(books.csv, authors.csv, books_authors.csv)

    def tearDown(self):
        pass

    #Tests for 2nd function: books: ValueError: valid author IDs
    
    def test_negative_author_ID(self):
        self.assertRaises(ValueError, self.source_checker.books, -4, None, None, None, "title")

    def test_big_author_ID(self):
        self.assertRaises(ValueError, self.source_checker.books, 312, None, None, None, "title")

if __name__ == '__main__':
    unittest.main()
