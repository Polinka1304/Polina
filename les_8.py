from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
import asyncio
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6375005495:AAGqk5wgSW45DI9gq-rM_sRRVB5y1Pvg4WU')
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    bt = [
        [types.KeyboardButton(text = 'Открыть веб страницу',web_app = WebAppInfo(url = 'https://polinka1304-psychic-space-journey-9r567g7755gfp646-8080.app.github.dev/index.html'))]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard = bt)
    await message.answer('Привет!!!', reply_markup = markup)





async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())