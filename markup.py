from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_Tema = KeyboardButton('Родитель👨🏻')
btn_2 = KeyboardButton('Ребенок👦🏻')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_Tema, btn_2)

button_1 = KeyboardButton('1.Артикуляционная гимнастика')
button_2 = KeyboardButton('2.Дыхательная гимнастика')
button_3 = KeyboardButton('3.Пальчиковая гимнастика')
button_4 = KeyboardButton('4.Мимическая гимнастика')
button_5 = KeyboardButton('5.Физ минутка')
button_back = KeyboardButton('Назад ➡')
ChildMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1, button_2, button_3, button_4, button_5, button_back)

button1 = KeyboardButton('1⃣')
button2 = KeyboardButton('2⃣')
button3 = KeyboardButton('3⃣')
button_back = KeyboardButton('Назад ➡')
ParentMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2, button3, button_back)

