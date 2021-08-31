# класс
# экземпляр класса
# атрибут класса
# атрибут экземпляра класса
# метод экземпляра класса
# ---------------------------
# наследование

from lesson15_classes import Book, TecBook

######################################################

book_1 = Book("King", "Dark tower", 100)
book_2 = Book("London", "Martin Iden", 123)
book_3 = TecBook("Skanavi", "Blabla", 600, "Math")

book_1.increase_current_page(12)
book_3.double_increase_current_page(5)

# print(book_1.author, book_1.page_count, book_1.current_page)
# print(book_3.author, book_3.ganre, book_3.current_page)

print(book_1)
print(book_3)

books = [book_1, book_2, book_3]

print(books)





#######################################################
# Book.author = "Леся Украинка"
# print(book_1.author, book_1.page_count)
# print(book_2.author, book_2.page_count)
# print("---------------------------------------")
# book_1.page_count = 100
# book_1.author = "King"
# book_1.title = "Dark tower"
# book_1.year = 1989

# Book.author = "Леся Украинка"
# print(book_1.author, book_1.page_count)
# print(book_2.author, book_2.page_count)

# print(book_1.author, book_1.page_count, book_1.year)
# print(book_2.author, book_2.page_count)