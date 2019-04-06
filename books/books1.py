import sys

def sort_books(file, how):
    print("sort_books")

def sort_authors(file, how):
    print("sort_authors")
    
def sort_reverse(list):
    #use list and reverse, print
    print("reverse print")

def main():
    file_object = open(sys.argv[1], "r")
    action = sys.argv[2]
    try:
        direction = sys.argv[3]
    except:
        direction = ""

    if action == "books": #sort by titles
        sort_books(file_object, direction)

    elif action == "authors": #sort by authors
        sort_authors(file_object, direction)
        
    else: #arguments not fitting
        print('Usage: blah blah blah', file=sys.stderr)
    
main()


