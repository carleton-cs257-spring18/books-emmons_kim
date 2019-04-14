#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018
    Modified by Eric Alexander, April 2019

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class.
'''

import csv, operator

class BooksDataSource:

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.books = books_filename
        self.authors = authors_filename
        self.books_authors = books_authors_link_filename

    @staticmethod
    def openfile(filename):
         with open(filename, newline = "") as csvfile:
             list = csv.reader(csvfile)
             sorted_list = sorted(list, key=operator.itemgetter(0))
             return sorted_list

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.)

            Raises ValueError if book_id is not a valid book ID.
        '''
        if book_id > 46 or book_id < 0:
            raise ValueError("what")
        else:
            sorted_list = BooksDataSource.openfile(self.books)
            for book in sorted_list:
                if book[0] == str(book_id):
                    return book[1]

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year

            See the BooksDataSource comment for a description of how a book is represented.

            QUESTION: Should Python interfaces specify TypeError?
            Raises TypeError if author_id, start_year, or end_year is non-None but not an integer.
            Raises TypeError if search_text or sort_by is non-None, but not a string.
				OUR ANSWER: Not for this assignment.

            QUESTION: How about ValueError? And if so, for which parameters?
            Raises ValueError if author_id is non-None but is not a valid author ID.
				OUR ANSWER: Yes, but just for author_id.
        '''
        return []

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)

            Raises ValueError if author_id is not a valid author ID.
        '''
        return {}

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        return []

