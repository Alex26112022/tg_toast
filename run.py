import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

