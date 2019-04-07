'''
Authors: Allison Kim and Madeleine Emmons
Date: April 7, 2019

This program allows a user to extract information from a csv file containing
book titles and authors, and use either one of the information to create
a list in forward or reverse alphabetical order. Command line arguments
in the correct format would print out sorted list.
'''

import sys, csv
import operator

'''
This function's parameters are a cvs filename that contains book titles and authors,
and a Boolean that checks whether the list should be alphabetical in ascending or
descending order. Its output is a printed list of book titles, either in alphabetical
or reverse alphabetical order.
'''
def sort_books(file, how):
    with open(file, newline = "") as csvfile:
        list = csv.reader(csvfile)
        #Sorts the items in the file by book title, column 1.
        sorted_books = sorted(list, key=operator.itemgetter(0))
        if how:
            for book in sorted_books: 
                print(book[0], sep = "\n")
        else:
            #Prints the list in reverse order.
            sorted_books.reverse()
            for book in sorted_books: 
                print(book[0], sep = "\n")

'''
This function's parameters are a cvs filename that contains book titles and authors,
and a Boolean that checks whether the list should be alphabetical in ascending or
descending order. Its output is a printed list of authors, either in alphabetical
or reverse alphabetical order.
'''
def sort_authors(filename, boolean):
    names = []
    with open(filename) as csvfile:
        books = csv.reader(csvfile, delimiter=",")
        #Loops through the file and extracts the authors' names 
        #from each row and adds them to a list. 
        for row in books:
            name = row[2].split(" (")
            name = name[0]
            names.append(name)
        #Sorts the books in alphabetical order by last name. 
        names = sorted(names, key = lambda x: x.split(" ")[-1])
        #Prints the list in reverse order. 
        if boolean == False:
            names_rev = []
            for y in names:
                names_rev.insert(0, y)
            for j in names_rev:
                print(j)
        else:
            for x in names:
                print(x)    

def main():
    #Catches command line argument error:
    #should include all 3 or 4 requirements.
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: blah blah blah', file=sys.stderr)
        
    else:
        file_object = sys.argv[1]

        try:
            action = sys.argv[2]
            
            #Makes sure csv file being called is valid.
            try:
                f = open(file_object)
            except FileNotFoundError:
               print('Usage: blah blah blah', file=sys.stderr)
               return

        except:
            print('Usage: blah blah blah', file=sys.stderr)
            return

        try:
            action = sys.argv[2]
        except:
            print('Usage: blah blah blah', file=sys.stderr)
            return
        
        try:
            #Using command line arguments, checks if list to be printed should be in
            #alphabetical or reverse alphabetical order.
            direction = sys.argv[3]
            if direction == "reverse":
                direction = False
            elif direction == "forward":
                direction = True
            else:
                print('Usage: blah blah blah', file=sys.stderr)
                return
                
        except:
            #The direction argument is not mandatory. Consider absent argument as
            #"forward".
            direction = True

        if action == "books":
            sort_books(file_object, direction)
            
        elif action == "authors":
            sort_authors(file_object, direction)
            
        else:
            print('Usage: blah blah blah', file=sys.stderr)
    
if __name__ == '__main__':
    main()


