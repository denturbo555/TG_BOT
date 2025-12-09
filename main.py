import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from config import TOKEN_BOT

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Токен бота
TOKEN = TOKEN_BOT

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Клавиатура с кнопкой "Привет"
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")]
    ],
    resize_keyboard=True
)

# Хэндлер на команду /start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Бот работает 👍🐧🐥🐤🦉🪸",
        reply_markup=keyboard
    )

# Хэндлер на кнопку "Привет"
@dp.message(F.text == "Привет")
async def hello_button(message: types.Message):
    await message.answer("Привет!")

# Главная функция запуска
async def main():
    logging.info("Бот запущен ✅")
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

# Запуск бота
if name == "main":
    asyncio.run(main())
