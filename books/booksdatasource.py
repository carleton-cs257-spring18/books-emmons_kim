import csv, operator

class BooksDataSource:

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.bookss = books_filename
        self.authorss = authors_filename
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
            books_list = BooksDataSource.openfile(self.bookss)
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
            linked_list = BooksDataSource.openfile(self.books_authors)
            books_list = BooksDataSource.openfile(self.bookss)
            ids = []
            books = []
            for linkids in linked_list:
                if linkids[1] == str(author_id):
                    ids.append(linkids[0])
            for id in ids:
                for book in books_list:
                    if book[0] == str(id):
                        books.append(book[1])
            return books
        
    ''' 
    Returns the author with the specified ID. 
    Raises ValueError if author_id is not a valid author ID.
    '''
    def author(self, author_id):
        if author_id > 24 or author_id < 0:
            raise ValueError("That is not a valid ID number.")
        else:
            authors_list = BooksDataSource.openfile(self.authorss)
            author_name = []
            for author in authors_list:
                if author[0] == str(author_id):
                    author_name.append(author[1])
                    author_name.append(author[2])
            return author_name
    
    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        if book_id != None:
            if book_id > 48 or book_id < 0:
                raise ValueError("That is not a valid ID number.")
            else:
                return[]
        else:
            if search_text != None:
                authors_list = BooksDataSource.openfile(self.authorss)
                author_list = []
                for author in authors_list:
                    author_name = []
                    if (author[1].lower().find(search_text.lower()) != -1 or
                        author[2].lower().find(search_text.lower()) != -1):
                        author_name.append(author[1])
                        author_name.append(author[2])
                        author_name.append(author[3])
                        author_list.append(author_name)
                if sort_by == "birth_year":
                    s_author_list = sorted(author_list, key=operator.itemgetter(2))
                else:
                    s_author_list = sorted(author_list, key=operator.itemgetter(0))
                only_name_list = []
                for each_author in s_author_list:
                    name_list = []
                    name_list.append(each_author[0])
                    name_list.append(each_author[1])
                    only_name_list.append(name_list)
                return only_name_list
            else:
                return []

'''
booksdatasource = BooksDataSource("books.csv", "authors.csv", "books_authors.csv")
print(booksdatasource.authors(search_text = "le", sort_by = "birth_year"))
print(booksdatasource.authors(search_text = "char"))
print(booksdatasource.authors(search_text = "w", sort_by = "value"))
'''
