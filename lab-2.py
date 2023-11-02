

# def books_1():
#     with open('books.csv','r') as fh:
#         count = 0
#         for string in fh:
#             my_book = string.split(';')
#             if len(my_book[1]) > 30:
#                 count += 1
#         print (count)

# print(books_1())


# def search_book():
#     list = []
#     author = input('Введите ФИО автора книги:\n')
#     with open('books.csv') as fh:
#         for string in fh:
#             my_book = string.split(';')
#             if my_book[4] == author and float(my_book[7]) >= 150:
#                 list.append(my_book[1])
#         print('Вот все книги автора, которые удалось найти согласно ограничению:\n')
#         for item in list:
#             print(item)
        
# print(search_book())


def bibliographic_search():
    from random import randrange
    result = [randrange(1, 9411) for x in range(20)]

    with open ('books.csv', 'r') as f:
        number = 0
        books = [0] * 20
        for string in f:
            my_book = string.split(';')
            for i in range(20):
                if number == result[i]:
                    books[i] = f'{my_book[3]}. {my_book[1]} - {my_book[6][6:10]}'
            number += 1

    with open ('result.txt', 'w') as fh:
        i = 0
        for num, line in enumerate(result):
            line = books[i]
            fh.write(f'{num + 1}. {line}\n')
            i += 1

print(bibliographic_search())

