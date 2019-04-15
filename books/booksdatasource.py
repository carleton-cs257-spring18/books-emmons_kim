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
            for book in books_list:
                for id in ids:
                    if book[0] == str(id):
                        books.append(book[1])
            return books

    @staticmethod
    def specifiedsort(author_list, sort_key):
        if sort_key == "birth_year":
            s_author_list = sorted(author_list, key=operator.itemgetter(2))
            check_authors = len(s_author_list)
            for position in range (0, check_authors-2):
                first_author = s_author_list[position]
                second_author = s_author_list[position+1]
                if (first_author[2] == second_author[2]
                    and first_author[0] > second_author[0]):
                    temp_author = first_author
                    s_author_list[position] = s_author_list[position+1]
                    s_author_list[position+1] = temp_author
        else:
            s_author_list = sorted(author_list, key=operator.itemgetter(0))
            check_authors = len(s_author_list)
            for position in range (0, check_authors-2):
                first_author = s_author_list[position]
                second_author = s_author_list[position+1]
                if (first_author[0] == second_author[0]
                    and first_author[1] > second_author[1]):
                    temp_author = first_author
                    s_author_list[position] = s_author_list[position+1]
                    s_author_list[position+1] = temp_author
        only_name_list = []
        for each_author in s_author_list:
            name_list = []
            name_list.append(each_author[0])
            name_list.append(each_author[1])
            only_name_list.append(name_list)
        return only_name_list

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
    
    def authors(self, *, book_id=None, search_text=None, start_year=None,
                end_year=None, sort_by='birth_year'):
        if book_id != None:
            if book_id > 48 or book_id < 0:
                raise ValueError("That is not a valid ID number.")
            else:
                book_author_list = BooksDataSource.openfile(self.books_authors)
                authors_list = BooksDataSource.openfile(self.authorss)
                author_ids = []
                author_list = []
                for book_author in book_author_list:
                    if book_author[0] == str(book_id):
                        author_ids.append(book_author[1])
                for author in authors_list:
                    author_name = []
                    for id in author_ids:
                        if author[0] == str(id):
                            author_name.append(author[1])
                            author_name.append(author[2])
                            author_name.append(author[3])
                            author_list.append(author_name)
        elif search_text != None:
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
        elif start_year != None:
            authors_list = BooksDataSource.openfile(self.authorss)
            author_list = []
            for author in authors_list:
                author_name = []
                if author[4] >= str(start_year) or author[4] == "NULL":
                    author_name.append(author[1])
                    author_name.append(author[2])
                    author_name.append(author[3])
                    author_list.append(author_name)
        elif end_year != None:
            authors_list = BooksDataSource.openfile(self.authorss)
            author_list = []
            for author in authors_list:
                author_name = []
                if author[3] <= str(end_year):
                    author_name.append(author[1])
                    author_name.append(author[2])
                    author_name.append(author[3])
                    author_list.append(author_name)
        return BooksDataSource.specifiedsort(author_list, sort_by)
