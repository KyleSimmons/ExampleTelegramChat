from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)
count = 150
pag_callback = CallbackData('current_state', 'current_page')

button_next_page = InlineKeyboardButton(text='next page', callback_data='next_page')
button_previous_page = InlineKeyboardButton(text='previous page', callback_data='previous_page')


def create_button(count, hand_name):
    buttons = []

    for i in range(count):
        buttons.append(InlineKeyboardButton(text='b' + str(i), callback_data=hand_name))

    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)

    if count > 100:
        keyboard.row(button_previous_page, button_next_page)

    return keyboard


@dp.message_handler(commands=['start'])
async def start_answer(message: types.Message):
    await message.reply('Count = ' + str(count) + ' Select a button:', reply_markup=create_button(count, 'one_handler'))


@dp.callback_query_handler(text=['one_handler', 'two_handler'])
async def com(call: types.CallbackQuery):
    if call.data == 'one_handler':
        await call.message.answer('Button One')
    if call.data == 'two_handler':
        await call.message.answer('Button Two')
    await call.answer()


executor.start_polling(dp)
