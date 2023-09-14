from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
from aiogram import F
import asyncio
import json
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6375005495:AAGqk5wgSW45DI9gq-rM_sRRVB5y1Pvg4WU')
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    bt = [
        [types.KeyboardButton(text = 'Открыть веб страницу',web_app = WebAppInfo(url = 'https://polinka1304.github.io/Polina/'))]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard = bt)
    await message.answer('Привет!!!', reply_markup = markup)


@dp.message(F.web_app_data)
async def web_app(message: types.Message):
    #from our app
    res = json.loads(message.web_app_data.data)
    await message.answer(f"Name: {res['name']}. Email: {res['email']}. Phone: {res['phone']}")




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
