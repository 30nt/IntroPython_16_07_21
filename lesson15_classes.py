class Book:
    def __init__(self, author, title, page_count):
        self.author = author
        self.title = title
        self.page_count = page_count
        self.current_page = 0

    def increase_current_page(self, pages=1):
        self.current_page += pages

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}"

    def __repr__(self):
        return f"({self.author}, {self.title})"


class TecBook(Book):
    def __init__(self, author, title, page_count, ganre):
        super(TecBook, self).__init__(author, title, page_count)
        self.ganre = ganre

    def __str__(self):
        answer = super().__str__()
        return f"{answer}, Ganre: {self.ganre}"

    def double_increase_current_page(self, pages=1):
        self.current_page += pages * 2
