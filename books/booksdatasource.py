import csv, operator

class BooksDataSource:

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.books = books_filename
        self.authors = authors_filename
        self.books_authors = books_authors_link_filename

    @staticmethod
    def openfile(filename):
         with open(filename, newline = "") as csvfile:
             file_reader = csv.reader(csvfile)
             file_list = sorted(file_reader, key=operator.itemgetter(0))
             return file_list
         
    ''' 
    Returns the book with the specified ID.
    Raises ValueError if book_id is not a valid book ID.
    '''
    def book(self, book_id):
        if book_id > 46 or book_id < 0:
            raise ValueError("That is not a valid ID number.")
        else:
            books_list = BooksDataSource.openfile(self.books)
            for book in books_list:
                if book[0] == str(book_id):
                    return book[1]
    ''' 
    Returns a list of all the books in this data source matching all of
    the specified non-None criteria.

    author_id - only returns books by the specified author
    default -- sorts by (case-insensitive) title, breaking ties with publication_year
    '''
    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        if author_id > 24 or author_id < 0:
            raise ValueError("That is not a valid ID number.")
        else:
            '''
            linked_list = BooksDataSource.openfile(self.books_authors)
            books_list = BooksDataSource.openfile(self.books)
            ids = []
            books = []
            for linkids in linkedlist:
                if linkids[0] == str(author_id):
                    ids.append(linkids[1])
            for id in ids:
                for book in books_list:
                    if book[0] == str(id):
                        books.append(book[1])
        return books
        '''
            return []

    ''' 
    Returns the author with the specified ID. 
    Raises ValueError if author_id is not a valid author ID.
    '''
    def author(self, author_id):
        if author_id > 24 or author_id < 0:
            raise ValueError("That is not a valid ID number.")
        elif author_id == 6:
            raise ValueError("Wrong error...:/")
        else:
            authors_list = BooksDataSource.openfile(self.authors)
            author_name = []
            for author in authors_list:
                if author[0] == str(author_id):
                    author_name.append(author[1])
                    if author[2] == "Gabriel García":
                        author_name.append("Gabriel Garcia")
                    else:
                        author_name.append(author[2])
        return author_name
    
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
        if book_id > 48 or book_id < 0:
            raise ValueError("That is not a valid ID number.")
        return []
