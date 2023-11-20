import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.choice_buttons import info, info_keyboard, less_info, no_info, all_categories, go_to_videos

from loader import dp, bot


@dp.message_handler(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text="Привет, мой приятный друг! Нажми, что хочешь сделать.", reply_markup=info)


@dp.callback_query_handler(lambda c: c.data == 'about_me')
async def showing_info(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Мне приятно, что ты хочешь узнать обо мне побольше. Что тебя интересует?",
                              reply_markup=info_keyboard)


@dp.callback_query_handler(lambda c: c.data == 'sticker')
async def process_callback_button3(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(callback_query.from_user.id, sticker='CAACAgIAAxkBAAEKwrNlVdSmXm4DgI1-RHFpfiQlXps7EQACjRgAAo3xMEjCF6lG7snpVTME')
    await bot.send_message(callback_query.from_user.id, "Принимай мой новый стикерпак и возвращайся!", reply_markup=do_back())

def do_back():
    back_button = InlineKeyboardMarkup().add(InlineKeyboardButton("Вернуться", callback_data="back"))
    return back_button


@dp.callback_query_handler(lambda c: c.data == 'back')
async def call_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Продолжаем!", reply_markup=less_info)


@dp.callback_query_handler(lambda c: c.data == 'go_back')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Что делаем дальше?", reply_markup=no_info)


@dp.callback_query_handler(lambda c: c.data == 'video')
async def go_to_video(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Давай помогу с выбором!", reply_markup=go_to_videos)


@dp.callback_query_handler(lambda c: c.data == 'categories')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Выбирай на здоровье!", reply_markup=all_categories)
