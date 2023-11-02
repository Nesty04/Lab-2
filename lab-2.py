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
#     with open('books.csv', 'r') as fh:
#         for string in fh:
#             my_book = string.split(';')
#             if my_book[4] == author and float(my_book[7]) >= 150:
#                 list.append(my_book[1])
#         print('Вот все книги автора, которые удалось найти согласно ограничению:\n')
#         for item in list:
#             print(item)
        
# print(search_book())


# def bibliographic_generator():
#     from random import randrange
#     result = [randrange(1, 9411) for x in range(20)]

#     with open ('books-en.csv', 'r') as f:
#         number = 0
#         books = [0] * 20
#         for string in f:
#             my_book = string.split(';')
#             for i in range(20):
#                 if number == result[i]:
#                     books[i] = f'{my_book[2]}. {my_book[1]} - {my_book[3]}'
#             number += 1

#     with open ('result.txt', 'w') as fh:
#         i = 0
#         for num, line in enumerate(result):
#             line = books[i]
#             fh.write(f'{num + 1}. {line}\n')
#             i += 1

# print(bibliographic_generator())


# def additional_task():
#     publishers = []
#     most_popular = []
#     with open('books-en.csv', 'r') as fh:
#         fisrt_line = fh.readline()
#         for string in fh:
#             my_book = string.split(';')
#             publishers.append(my_book[4])
#             name, downloads = str(my_book[1]), int(my_book[-2])
#             most_popular += [[name, downloads]]
#         most_popular.sort(key = lambda k:k[1], reverse = True)

#         print('Издетельства:', set(publishers))

#         print('Самые поплярные книги:')
#         for i in range(20):
#             print(f'{i + 1}. {most_popular[i][0]}')
        
# print(additional_task())
