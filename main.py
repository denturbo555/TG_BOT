import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from config import TOKEN_BOT

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

TOKEN = TOKEN_BOT

# Правильно!
bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Бот работает 👍🐧🐥🐤🦉🪸",
        reply_markup=keyboard
    )

@dp.message(F.text == "Привет")
async def hello_button(message: types.Message):
    await message.answer("Привет!")

async def main():
    logging.info("Бот запущен ✅")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
