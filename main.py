import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6944012562:AAFU8IhmdBy0epN7yYrmOPfiTQBraszJbmU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Узнать о тебе!", callback_data='button1')
    button2 = InlineKeyboardButton("Покажи видео!", url='https://www.youtube.com/watch?v=jMfrWa0wuTw')
    button3 = InlineKeyboardButton("Хочу стикеры!", callback_data='button3')
    keyboard.row(button1, button2, button3)

    await message.answer("Привет, мой приятный друг! Нажми, что хочешь сделать.", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    # Отправляем новое сообщение с текстом и четырьмя кнопками, одна из которых возвращает пользователя назад
    await bot.send_message(callback_query.from_user.id, "Теперь узнаем о вас! Выберите действие:",
                           reply_markup=create_new_keyboard())

def create_new_keyboard():
    new_keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Действие 1", callback_data='action1')
    button2 = InlineKeyboardButton("Действие 2", callback_data='action2')
    button3 = InlineKeyboardButton("Действие 3", callback_data='action3')
    back_button = InlineKeyboardButton("Назад", callback_data='back')
    new_keyboard.row(button1, button2, button3, back_button)
    return new_keyboard

@dp.callback_query_handler(lambda c: c.data in ['action1', 'action2', 'action3', 'back'])
async def process_new_keyboard(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    if callback_query.data == 'back':
        # Если нажата кнопка "Назад", возвращаем пользователя к первой клавиатуре
        await bot.send_message(callback_query.from_user.id, "Возврат назад.",
                               reply_markup=create_initial_keyboard())
    else:
        # В противном случае отправляем сообщение о том, на какую кнопку новой клавиатуры нажали
        await bot.send_message(callback_query.from_user.id, f"Вы выбрали {callback_query.data}.")

def create_initial_keyboard():
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Узнать о тебе!", callback_data='button1')
    button2 = InlineKeyboardButton("Покажи видео!", url='https://www.youtube.com/watch?v=jMfrWa0wuTw')
    button3 = InlineKeyboardButton("Хочу стикеры!", callback_data='button3')
    keyboard.row(button1, button2, button3)
    return keyboard

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)