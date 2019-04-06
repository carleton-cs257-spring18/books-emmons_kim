import sys, csv

def sort_books(file, how):
    print("sort_books")

def sort_authors(file, how):
    print("sort_authors")
    
def sort_reverse(list):
    #use list and reverse, print
    print("reverse print")

def main():    
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: blah blah blah', file=sys.stderr)
        
    else:
        try:
            file_object = open(sys.argv[1], "r")
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


