#23 tests

import booksdatasource, unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.source_checker = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

    def tearDown(self):
        pass

    #Tests for 1st function: book: 3

    def test_small_book_id(self):
       self.assertRaises(ValueError, self.source_checker.book, -34)

    def test_big_book_id(self):
        self.assertRaises(ValueError, self.source_checker.book, 49)

    def test_book_match(self):
        self.assertEqual(self.source_checker.book(16),"Omoo")

    #Tests for 2nd function: books: 3
    
    def test_small_author_id(self):
        self.assertRaises(ValueError, self.source_checker.books, author_id=-4)

    def test_big_author_id(self):
        self.assertRaises(ValueError, self.source_checker.books, author_id=312)

    def test_books_match(self):
        self.assertEqual(self.source_checker.books(author_id=13), ["Moby Dick", "Omoo"])

    #Tests for 3rd function: author: 3

    #Tests for 4th function: authors: 14

    #book_id: 5

    '''
    def test_small_book_id(self):
    def test_big_book_id(self):  
    '''
    
    def test_authors_default_match(self):
        self.assertEqual(self.source_checker.authors(book_id=23), ["Wodehouse", "Pelham Grenville"])
    
    def test_authors_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(book_id=6), [["Pratchett", "Terry"], ["Gaiman", "Neil"]])

    def test_authors_other_value_match(self):
        self.assertEqual(self.source_checker.authors(book_id=6), [["Gaiman", "Neil"], ["Pratchett", "Terry"]])

    #search_text: 3

    def test_search_text_default_match(self):
        self.assertEqual(self.source_checker.authors(search_text="char"), [["Brontë", "Charlotte"], ["Dickens", "Charles"]])

    def test_search_text_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(search_text="le", sort_by="birth_year"), [["Lewis", "Sinclair"], ["Lewis", "Sinclair"], ["Carré", "John Le"]])
        
    def test_search_text_other_value_match(self):
        self.assertEqual(self.source_checker.authors(search_text="w", sort_by="value"), [["Cather", "Willa"], ["Willis", "Connie"], ["Wodehouse", "Pelham Grenville"]])

    #start_year: 3

    #end_year: 3
    
if __name__ == '__main__':
    unittest.main()

#Test out author and book ids again?
#Test for unmatch also?
#What do you mean by other value?
#What about repeated names?
                                    
