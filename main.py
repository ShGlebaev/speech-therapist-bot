from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config
import markup as nav
from readtext import randomtext

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}! Я твой помощник. '
                                                 'Что ты хочешь сегодня поделать?'.format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Ребенок👦🏻":
        await bot.send_message(message.from_user.id, '1.Артикуляционная гимнастика\n'
                                                     '2.Дыхательная гимнастика\n'
                                                     '3.Пальчиковая гимнастика\n'
                                                     '4.Мимическая гимнастика\n'
                                                     '5.Физ минутка\n'
                                                     , reply_markup=nav.ChildMenu)
    elif message.text == "Назад ➡":
        g = randomtext()
        await bot.send_message(message.from_user.id, f'{g[0]}', reply_markup=nav.mainMenu)

    elif message.text == "Родитель👨🏻":
        await bot.send_message(message.from_user.id, '1.Запись к логопеду\n'
                                                     '2.Логобуклета\n'
                                                     '3.Как проводить занятия\n'
                                                     , reply_markup=nav.ParentMenu)
    elif message.text == "1.Артикуляционная гимнастика":
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=UTvjhpdVHDM')
    elif message.text == "2.Дыхательная гимнастика":
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=H6w8QmmBwaI')
    elif message.text == "3.Пальчиковая гимнастика":
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=GZQz0ugAexc')
    elif message.text == "4.Мимическая гимнастика":
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=jIx43EJz_4A')
    elif message.text == "5.Физ минутка":
        await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=EjX5MUHjSIo')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)