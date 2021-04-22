import csv
from json import loads, dumps


class TestMakeResult:
    def test_write_result(self):
        """Метод сохранения результата в файл result.json"""
        with open('../files/result.json', 'w') as file:
            result_list = self.get_result_list()
            s = dumps(result_list, indent=2)
            file.write(s)

    def get_result_list(self):
        """Метод формирования справочника result_list для файла result.json"""
        users = self.get_all_users()
        books = self.get_general_books_info()
        result_list = []
        for i, user in enumerate(users):
            result_list.append({"name": user["name"],
                                "gender": user["gender"],
                                "address": user["address"],
                                "books": books[i] if i < len(books) else []
                                })
        return result_list

    def get_all_users(self):
        """Метод преобразования данных из файла users.json в список словарей users"""
        with open('../files/users.json', 'r') as file:
            j = file.read()
            all_users = loads(j)
            return all_users

    def get_all_books(self):
        """Метод преобразования данных из файла books.csv в словарь all_books"""
        with open('../files/books.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            all_books = []
            for item in reader:
                all_books.append(dict(zip(header, item)))
        return all_books

    def get_general_books_info(self):
        """Метод выборки данных из справочника книг"""
        books = self.get_all_books()
        res_books = []
        for i, book in enumerate(books):
            res_books.append({"title": book["Title"],
                              "author": book["Author"],
                              "height": book["Height"]
                              })
        return res_books
