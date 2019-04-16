'''
Alison Kim
Madeleine Emmons
April 15, 2019
This program allows the user to do four things: 1. Search for the title of a book by its book ID,
2. Search for the name of the author by his or her author ID, 3. Sort a list of books written by an author
specified by an author ID (by title), or 4. Sort a list of authors by one of these input attributes, 
book ID, some search text, birth year, or end year (by birth year or last name). The user is required
to oragnized three files for this program. These must be csv files, one containing information about
books and their IDs, a similar one about authors and their IDs, and a "combined" file that matches
book IDs to their respective author IDs.
'''

import csv, operator

class BooksDataSource:
    
    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        self.bookss = books_filename # Variable with extra s prevents variable name mix up 
        self.authorss = authors_filename
        self.books_authors = books_authors_link_filename
        
    '''
    This funtion opens a csv file and turns it into a list. Each element in the list contains
    a list of row information: for example, author_id, last_name, first_name, birth_year, and end_year.
    '''
    @staticmethod
    def openfile(filename):
         with open(filename, newline = "") as csvfile:
             file_reader = csv.reader(csvfile)
             file_list = sorted(file_reader, key=operator.itemgetter(0))
             return file_list
    
    '''
    The function takes in an integer that represents a book ID. If the integer is not valid,
    if the ID is not contained in the books file (bookss), the function will raise a ValueRrror.
    If the integer is valid, the function returns the title of the book corresponding to the ID.
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
    This compound function takes in an author_id, search_text string, start_year, end_year or a sort_by method. 
    For this assignment, we are only considering author_id as a valid input. A ValueError is rasied if and only
    if the author ID is not contained in the authors file (authorss). The function returns a list of books 
    based on the author id. The books are automatically sorted by title.
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
 
    '''
    The function takes in an integer that represents an author ID. If the integer is not valid,
    if the ID is not contained in the authors file, the function will raise a ValueRrror.
    If the integer is valid, the function returns the author's name corresponsing to the ID.
    '''
    def author(self, author_id):
        if author_id > 24 or author_id < 0:
            raise ValueError("That is not a valid ID number.")
        else:
            authors_list = BooksDataSource.openfile(self.authorss)
            author_name = []
            for author in authors_list:
                if author[0] == str(author_id):
                    author_name.append(author[1]) # An author's name is returned as a list:
                    author_name.append(author[2]) # [last name, first name]
            return author_name
        
    '''
    This function allows a list of author's names and birth years to be sorted by the authors' 
    birth years or alphbetically by their last names based on the input in the parameter. If two 
    authors have the same birth years, their names would be sorted by their last names again. 
    If two authors have the same last names, their names would be sorted by their first names.
    '''
    @staticmethod
    def specifiedsort(author_list, sort_key):
        if sort_key == "birth_year": # This applies to default sort_key also
            s_author_list = sorted(author_list, key=operator.itemgetter(2)) # First sort by birth year
            check_authors = len(s_author_list)
            for position in range (0, check_authors-2):
                first_author = s_author_list[position]
                second_author = s_author_list[position+1]
                if (first_author[2] == second_author[2]
                    and first_author[0] > second_author[0]): # Check if names should be sorted again
                    temp_author = first_author               # Now, sort_key = last name
                    s_author_list[position] = s_author_list[position+1]
                    s_author_list[position+1] = temp_author # Swap
        else:
            s_author_list = sorted(author_list, key=operator.itemgetter(0)) # First sort by last name
            check_authors = len(s_author_list)
            for position in range (0, check_authors-2):
                first_author = s_author_list[position]
                second_author = s_author_list[position+1]
                if (first_author[0] == second_author[0]
                    and first_author[1] > second_author[1]): # Now, sort_key = first name
                    temp_author = first_author
                    s_author_list[position] = s_author_list[position+1]
                    s_author_list[position+1] = temp_author
        only_name_list = []
        for each_author in s_author_list: # Exclude birth years from authors' information
            name_list = []
            name_list.append(each_author[0])
            name_list.append(each_author[1])
            only_name_list.append(name_list)
        return only_name_list
    
    '''
    This function returns a list of authors that consists of authors based on the specifications 
    provided in the parameters. It takes in a book_id, search_text, start_year, or end_year, 
    along with a sorting method. A ValueError is rasied if and only if the book ID is not contained
    in the books file.
    '''
    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        author_list = []
        if book_id != None:
            if book_id > 48 or book_id < 0:
                raise ValueError("That is not a valid ID number.")
            else: # book_id returns a list of authors who coauthored the specified book
                book_author_list = BooksDataSource.openfile(self.books_authors)
                authors_list = BooksDataSource.openfile(self.authorss)
                author_ids = []
                for book_author in book_author_list:
                    if book_author[0] == str(book_id):
                        author_ids.append(book_author[1])
                for author in authors_list:
                    author_name = []
                    for id in author_ids:
                        if author[0] == str(id):
                            author_name.append(author[1])
                            author_name.append(author[2])
                            author_name.append(author[3])   # Chose to include birth year so that
                            author_list.append(author_name) # we could later sort names by birth year
        elif search_text != None: # search_text returns a list of authors with last or first name containing specified phrase
            authors_list = BooksDataSource.openfile(self.authorss) # (not case sensitive)
            for author in authors_list:
                author_name = []
                if (author[1].lower().find(search_text.lower()) != -1 
                    or author[2].lower().find(search_text.lower()) != -1):
                    author_name.append(author[1])
                    author_name.append(author[2])
                    author_name.append(author[3])
                    author_list.append(author_name)
        elif start_year != None: # start_year returns a list of authors who were or are still alive after specified year
            authors_list = BooksDataSource.openfile(self.authorss)
            for author in authors_list:
                author_name = []
                if author[4] >= str(start_year) or author[4] == "NULL":
                    author_name.append(author[1])
                    author_name.append(author[2])
                    author_name.append(author[3])
                    author_list.append(author_name)
        elif end_year != None: # end_year returns a list of authors who were or have been alive til the specified year
            authors_list = BooksDataSource.openfile(self.authorss)
            for author in authors_list:
                author_name = []
                if author[3] <= str(end_year):
                    author_name.append(author[1])
                    author_name.append(author[2])
                    author_name.append(author[3])
                    author_list.append(author_name)
        return BooksDataSource.specifiedsort(author_list, sort_by)
