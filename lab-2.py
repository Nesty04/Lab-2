

def books():
    with open('books-en.csv','r') as fh:
        count = 0
        for string in fh:
            my_book = string.split(';')
            if len(my_book[1]) > 30:
                count += 1
        print (count)
            

print(books())