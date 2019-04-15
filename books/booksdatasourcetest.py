'''
Authors: Allison Kim and Madeleine Emmons
Date: April 12, 2019

These are combinations of 23 unit tests for booksdatasource.py.
The tests check whether ValueErrors (TypeErrors are not included)
are raised at the correct spots and whether value returned from
all four functions match the expected outputs.
'''

import booksdatasource, unittest

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.source_checker = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

    def tearDown(self):
        pass

    #Tests for function book

    def test_small_book_id(self):
       self.assertRaises(ValueError, self.source_checker.book, -34)

    def test_big_book_id(self):
        self.assertRaises(ValueError, self.source_checker.book, 49)

    def test_book_match(self):
        self.assertEqual(self.source_checker.book(16),"Omoo")

    #Tests for function books
    
    def test_small_author_id_books(self):
        self.assertRaises(ValueError, self.source_checker.books, author_id = -4)

    def test_big_author_id_books(self):
        self.assertRaises(ValueError, self.source_checker.books, author_id = 312)

    def test_books_match_books(self):
        self.assertEqual(self.source_checker.books(author_id = 13), ["Moby Dick", "Omoo"])

    #Tests for function author

    def test_small_author_id(self):
        self.assertRaises(ValueError, self.source_checker.author, -6)

    def test_big_author_id(self):
        self.assertRaises(ValueError, self.source_checker.author, 600)
    
    def test_author_match(self):
        self.assertEqual(self.source_checker.author(9), ["Márquez", "Gabriel García"])

    #Tests for function authors

    #Tests for parameter book_id

    def test_small_book_id_authors(self):
        self.assertRaises(ValueError, self.source_checker.book, -786)
        
    def test_big_book_id_authors(self):
        self.assertRaises(ValueError, self.source_checker.book, 67)
    
    def test_authors_default_match(self):
        self.assertEqual(self.source_checker.authors(book_id = 23), [["Wodehouse", "Pelham Grenville"]])
    
    def test_authors_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(book_id = 6, sort_by = "birth_year"), [["Pratchett", "Terry"], ["Gaiman", "Neil"]])

    def test_authors_other_value_match(self):
        self.assertEqual(self.source_checker.authors(book_id = 6, sort_by = "value"), [["Gaiman", "Neil"], ["Pratchett", "Terry"]])

    #Tests for parameter search_text

    def test_search_text_default_match(self):
        self.assertEqual(self.source_checker.authors(search_text = "char"), [['Dickens', 'Charles'], ['Brontë', 'Charlotte']])

    def test_search_text_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(search_text = "le", sort_by = "birth_year"), [['Dickens', 'Charles'], ['Melville', 'Herman'], ['Wodehouse', 'Pelham Grenville'], ['Lewis', 'Sinclair'], ['Lewis', 'Sinclair'], ['Carré', 'John Le']])
        
    def test_search_text_other_value_match(self):
        self.assertEqual(self.source_checker.authors(search_text = "w", sort_by = "value"), [['Cather', 'Willa'], ['Lewis', 'Sinclair'], ['Lewis', 'Sinclair'], ['Willis', 'Connie'], ['Wodehouse', 'Pelham Grenville']])

    #Tests for parameter start_year

    def test_start_year_default_match(self):
        self.assertEqual(self.source_checker.authors(start_year = 1960), [["Alderman", "Naomi"], ["Bujold", "Lois McMaster"], ["Carré", "John Le"], ["Christie", "Agatha"], ["DuMaurier", "Daphne"], ["Gaiman", "Neil"], ["Jemisen", "N.K."], ["Lewis", "Sinclair"], ["Murakami", "Haruki"], ["Márquez", "Gabriel García"], ["Morrison", "Toni"], ["Pratchett", "Terry"], ["Rushdie", "Salman"], ["Willis", "Connie"], ["Wodehouse", "Pelham Grenvile"]])

    def test_start_year_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(start_year = 2000, sort_by = "birth_year"),[["Lewis", "Sinclair"], ["Márquez", "Gabriel Garcia"], ["Carré", "John Le"], ["Morrison", "Toni"], ["Willis", "Connie"], ["Rushdie", "Salman"], ["Bujold", "Lois McMaster"], ["Murakami", "Haruki"], ["Prachett", "Terry"], ["Gainman", "Neil"],  ["Bujold", "Lois McMaster"], ["Jemisen", "N.K."], ["Alderman", "Naomi"]])
    
    def test_start_year_other_value_match(self):
        self.assertEqual(self.source_checker.authors(start_year = 2019, sort_by = "value"), [["Alderman", "Naomi"], ["Bujold", "Lois McMaster"], ["Carré", "John Le"], ["Gaiman", "Neil"], ["Jemisen", "N.K."], ["Lewis", "Sinclair"], ["Murakami", "Haruki"],  ["Morrison", "Toni"],  ["Rushdie", "Salman"], ["Willis", "Connie"]]) 

    #Tests for parameter end_year

    def test_end_year_default_match(self):
        self.assertEqual(self.source_checker.authors(end_year = 1861), [["Austen", "Jane"], ["Brontë", "Ann"], ["Brontë", "Charlotte"], ["Bujold", "Lois McMaster"], ["Christie", "Agatha"], ["Dickens", "Charles"], ["Eliot", "George"], ["Jerome", "Jerome K."], ["Melville", "Herman"], ["Rushdie", "Salman"]])

    def test_end_year_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(end_year = 1820, sort_by = "birth_year"), [["Austen", "Jane"], ["Dickens", "Charles"], ["Brontë", "Charlotte"], ["Eliot", "George"], ["Melville", "Herman"], ["Brontë", "Ann"], ["Brontë", "Emily"]])
    
    def test_end_year_other_value_match(self):
        self.assertEqual(self.source_checker.authors(end_year = 1816, sort_by = "value"), [["Austen", "Jane"], ["Brontë", "Charlotte"], ["Dickens", "Charles"]])
    
if __name__ == '__main__':
    unittest.main()
