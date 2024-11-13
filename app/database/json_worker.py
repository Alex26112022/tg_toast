import json


class JsonWorker:
    """ Класс взаимодействия с json-файлом. """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_json(self, content: dict):
        """ Загружает данные в json-файл. """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(content, file, ensure_ascii=False, indent=4)
        print('Данные успешно записаны в json-файл!\n')

    def read_json(self):
        """ Считывает данные с json-файла. """
        item = None
        try:
            with open(self.file_path, encoding='utf-8') as file:
                item = json.load(file)
        except FileNotFoundError:
            print('Такого файла не существует!')
        return item
