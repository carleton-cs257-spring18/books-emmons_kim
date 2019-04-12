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
    
    def test_small_author_id_books(self):
        self.assertRaises(ValueError, self.source_checker.books, author_id=-4)

    def test_big_author_id_books(self):
        self.assertRaises(ValueError, self.source_checker.books, author_id=312)

    def test_books_match_books(self):
        self.assertEqual(self.source_checker.books(author_id=13), ["Moby Dick", "Omoo"])

    #Tests for 3rd function: author: 3

    def test_small_author_id(self):
        self.assertRaises(ValueError, self.source_checker.author, 6)

    def test_big_author_id(self):
        self.assertRaises(ValueError, self.source_checker.author, 600)
    
    def test_author_match(self):
        self.assertEqual(self.source_checker.author(9), ["Márquez", "Gabriel Garcia"])

    #Tests for 4th function: authors: 14

    #book_id: 5

    def test_small_book_id_authors(self):
        self.assertRaises(ValueError, self.source_checker.book, -786)
        
    def test_big_book_id_authors(self):
        self.assertRaises(ValueError, self.source_checker.book, 67)
    
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

    def test_start_year_default_match(self):
        self.assertEqual(self.source_checker.authors(start_year=1960), [["Alderman", "Naomi"], ["Bujold", "Lois McMaster"], ["Carré", "John Le"], ["Christie", "Agatha"], ["DuMaurier", "Daphne"], ["Gaiman", "Neil"], ["Jemisen", "N.K."], ["Lewis", "Sinclair"], ["Murakami", "Haruki"], ["Márquez", "Gabriel García"], ["Morrison", "Toni"], ["Pratchett", "Terry"], ["Rushdie", "Salman"], ["Willis", "Connie"], ["Wodehouse", "Pelham Grenvile"]])

    def test_start_year_birth_year_match(self):
        self.assertEqual(self.source_checker.authors(start_year = 2000, sort_by = "birth_year"),[["Lewis", "Sinclair"], ["Márquez", "Gabriel Garcia"], ["Carré", "John Le"], ["Morrison", "Toni"], ["Willis", "Connie"], ["Rushdie", "Salman"], ["Bujold", "Lois McMaster"], ["Murakami", "Haruki"], ["Prachett", "Terry"], ["Gainman", "Neil"],  ["Bujold", "Lois McMaster"], ["Jemisen", "N.K."], ["Alderman", "Naomi"]])
    
    def test_start_year_other_value_match(self):
        self.assertEqual(self.source_checker.authors(start_year = 2019, sort_by = "value"), [["Alderman", "Naomi"], ["Bujold", "Lois McMaster"], ["Carré", "John Le"], ["Gaiman", "Neil"], ["Jemisen", "N.K."], ["Lewis", "Sinclair"], ["Murakami", "Haruki"],  ["Morrison", "Toni"],  ["Rushdie", "Salman"], ["Willis", "Connie"]]) 

    #end_year: 3

    def test_end_year_default_match(self):
        self.assertEqual(self.source_checker.authors(end_year=1861), [["Austen", "Jane"], ["Brontë", "Ann"], ["Brontë", "Charlotte"], ["Bujold", "Lois McMaster"], ["Christie", "Agatha"], ["Dickens", "Charles"], ["Eliot", "George"], ["Jerome", "Jerome K."], ["Melville", "Herman"], ["Rushdie", "Salman"]])
    
if __name__ == '__main__':
    unittest.main()
