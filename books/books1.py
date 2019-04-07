import sys, csv
import operator

def sort_books(file, how):
    with open(file, newline = "") as csvfile:
        list = csv.reader(csvfile)
        sorted_books = sorted(list, key=operator.itemgetter(0))
        if how:
            for book in sorted_books: 
                print(book[0], sep = "\n")
        else:
            sorted_books.reverse()
            for book in sorted_books: 
                print(book[0], sep = "\n")

#This function takes in a cvs filename that contains book titles and 
# as well as taking in a boolean. Its output is a printed list of authors 
# in alphabetical order or reverse alphabetical order depending on if the 
# boolean is true or false respectively. 
def sort_authors(filename, boolean):
    names = []
    with open(filename) as csvfile:
        books = csv.reader(csvfile, delimiter=",")
        #This loop goes through the csv file and extracts the quthors name 
        #from each row and adds them to a list. 
        for row in books:
            name = row[2].split(" (")
            name = name[0]
            names.append(name)
        #Sorts the books in alphabetical order by last name. 
        names = sorted(names, key = lambda x: x.split(" ")[-1])
        #Prints the list in reverse. 
        if boolean == False:
            names_rev = []
            for y in names:
                names_rev.insert(0, y)
            for j in names_rev:
                print(j)
        #Prints the list forward. 
        else:
            for x in names:
                print(x)    

def main():    
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: blah blah blah', file=sys.stderr)
        
    else:
        try:
            file_object = sys.argv[1]
        except:
            print('Usage: blah blah blah', file=sys.stderr)
            return

        try:
            action = sys.argv[2]
        except:
            print('Usage: blah blah blah', file=sys.stderr)
            return
        
        try:
            direction = sys.argv[3]
            if direction == "reverse":
                direction = False #direction is a Boolean
            elif direction == "forward":
                direction = True
            else:
                print('Usage: blah blah blah', file=sys.stderr)
                return
            
        except:
            direction = True

        if action == "books": #sort by titles
            sort_books(file_object, direction)
            
        elif action == "authors": #sort by authors
            sort_authors(file_object, direction)
            
        else: #arguments not fitting
            print('Usage: blah blah blah', file=sys.stderr)
    
main()


