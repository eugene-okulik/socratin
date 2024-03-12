class BookClass:
    material = "Бумага"
    flag_text = True

    def __init__(self, name_book, author, count_pages, isbn, is_reserved):
        self.name_book = name_book
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


book1 = BookClass("Лев", "Неверующий", "651", "ISBN1", False)
book2 = BookClass("Книга мудрости", "Самоделкин", "657", "ISBN2", False)
book3 = BookClass("Княгиня", "Лермонтов", "66777", "ISBN3", False)
book4 = BookClass("Кирпич", "Достоевский", "768787", "ISBN4", False)
book5 = BookClass("Корона", "Ленин", "678", "ISBN5", False)
book3.is_reserved = True

for book in [book1, book2, book3, book4, book5]:
    result = f"Название книги: {book.name_book}, Автор: {book.author}, страниц: {book.count_pages}"
    if book.is_reserved:
        result += ", зарезервирована"
    print(result)


class TeachBook(BookClass):
    def __init__(self, name_book, author, count_pages, isbn, is_reserved, predmet, class_room, have_task):
        super().__init__(name_book, author, count_pages, isbn, is_reserved)
        self.predmet = predmet
        self.class_room = class_room
        self.have_task = have_task


teach_book1 = TeachBook("geo", "Панаморев", "657", "ISBN1", False, "Информатика", "9а", True)
teach_book2 = TeachBook("informatica", "Сидоров", "657", "ISBN1", True, "Информатика", "10б", False)
teach_book3 = TeachBook("biology", "Иванов", "657", "ISBN1", False, "Информатика", "3г", False)

for book in [teach_book1, teach_book2, teach_book3]:
    result = (f"Название: {book.name_book}, Автор: {book.author}, страниц: {book.count_pages}, "
              f"предмет: {book.predmet}, "
              f"класс: {book.class_room}")
    if book.is_reserved:
        result += ", зарезервирована"
    print(result)
