import asyncio
import logging

from app.database.json_worker import JsonWorker
from app.database.models import async_run_db, async_session, Theme, Toast
from app.database.parser import Parser
from config import path_json


def get_json_db():
    """ Возвращает json данные для БД. """
    parser = Parser()
    parser.load_content()
    json_data = parser.get_content()

    worker = JsonWorker(path_json)
    worker.load_json(json_data)
    json_db = worker.read_json()
    return json_db


js_data = get_json_db()


async def insert_workers(json_data: dict):
    async with async_session() as session:
        list_data = []
        theme_id = 1
        for theme, toasts in json_data.items():
            list_data.append(Theme(id=theme_id, title=theme))
            for toast in toasts:
                list_data.append(Toast(theme_id=theme_id, content=toast))
            theme_id += 1

        session.add_all(list_data)

        await session.commit()


async def get_update_db():
    await async_run_db()
    await insert_workers(js_data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(get_update_db())
    except KeyboardInterrupt:
        print("Exit")
