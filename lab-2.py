def books():
    with open('books-en.csv','r') as fh:
        for string in fh:
            count = 0
            my_book = [string.split(';')]
            print(my_book)
            if len(my_book[1]) > 30:
                count += 1
                print(my_book[1])