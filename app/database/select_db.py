import asyncio
import random

from sqlalchemy import select

from models import async_session, Toast


class SelectDb:
    """ Делает выборку из БД. """

    @staticmethod
    async def select_random_toast(theme_id: int):
        """ Выбирает случайный тост по теме. """
        async with async_session() as session:
            query = select(Toast).filter_by(theme_id=theme_id)
            result = await session.execute(query)
            toasts = result.scalars().all()
            return random.choice(toasts)
