import sys, csv

def sort_books(file, how):
    with open(file, newline = "") as csvfile:
        sorted_books = csv.reader(csvfile)
        if how:
            print(*sorted_books, sep = "\n")
        else:
            sort_reverse(sorted_books)

def sort_authors(file, how):
    sorted_authors = ["sorted", "authors"]
    if how:
        print(*sorted_authors, sep = "\n")
    else:
        sort_reverse(sorted_authors)
    
def sort_reverse(list):
    #csv reader is not a list
    list.reverse()
    print(*list, sep = "\n")

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


