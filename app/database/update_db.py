from app.database.json_worker import JsonWorker
from app.database.parser import Parser
from config import path_json


def update_db():
    """ Обновляет БД. """
    parser = Parser()
    parser.load_content()
    json_data = parser.get_content()

    worker = JsonWorker(path_json)
    worker.load_json(json_data)
    json_db = worker.read_json()


if __name__ == '__main__':
    update_db()
