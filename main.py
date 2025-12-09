import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from config import TOKEN_BOT

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
) #Логирование🤷‍♂️

TOKEN = TOKEN_BOT

bot = Bot(token=TOKEN) #токен бота
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")]
    ],
    resize_keyboard=True
) #Кнопка пользователя "Привет"

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет бот работает 👍🐧🐥🐤🦉🪸",
        reply_markup=keyboard
    )

@dp.message(F.text == "Привет")
async def hello_button(message: types.Message):
    await message.answer(("Привет!"))

async def main():
    print("Бот запущен👍🐧😂🐤🤣🪸😒😍😊❤️🐥🦉")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())