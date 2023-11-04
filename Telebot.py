import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="&&&&&&")

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hi!Я стартовый бот, больше информации по комманде /help")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Я простой бот который ничего не делает.")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

