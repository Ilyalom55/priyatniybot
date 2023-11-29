from pytube import Playlist
import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.eat_choice import eat_list, drinks
from keyboards.inline.choice_buttons import info, info_keyboard, less_info, no_info, all_categories, go_to_videos, eat, \
    end

from loader import dp, bot

@dp.message_handler(Command("start"))
async def cmd_start(message: Message):
    await bot.send_animation(message.from_user.id, r'https://media.tenor.com/9gNWL-w1CiQAAAAC/иэтонешутка-its-not-a-joke.gif', caption="Доброго времени суток, мой приятный друг, рад тебя видеть!💗 Нажми, что хочешь сделать👇", reply_markup=info)
    await message.delete()



@dp.callback_query_handler(lambda c: c.data == 'about_me')
async def showing_info(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await call.message.answer("Мне приятно, что ты хочешь узнать обо мне побольше. Здесь ты сможешь найти ссылки на мои соц.сети и сайт с уникальным мерчем 😎",
                              reply_markup=info_keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'sticker')
async def process_callback_button3(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    sticker_link = 'https://t.me/addstickers/YGOLOK_SMEHA'
    text_with_sticker = f"Забирай мой новый стикерпак 👉 {sticker_link} и возвращайся🫶"
    await bot.send_message(callback_query.from_user.id, text=text_with_sticker, reply_markup=do_back())
    await callback_query.message.delete()
def do_back():
    back_button = InlineKeyboardMarkup().add(InlineKeyboardButton("Вернуться🔙", callback_data="back"))
    return back_button


@dp.callback_query_handler(lambda c: c.data == 'back')
async def call_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Поздравляю, у тебя есть мои уникальные стикеры!\n Теперь ты можешь узнать больше о моих соц.сетях или перейти к выбору видео 🎬", reply_markup=less_info)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'go_back')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Забирай стикерпак или переходи к видео 🎬", reply_markup=no_info)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'video')
async def go_to_video(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Жмякай на кнопки👇, ну а я помогу с выбором🤗 ", reply_markup=go_to_videos)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'categories')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Выбирай на здоровье!", reply_markup=all_categories)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'back_to_choice')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Выбирай на здоровье!", reply_markup=go_to_videos)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'men_women')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Мужское/Женское👫 \n https://www.youtube.com/watch?v=gASBs8pRtLU", reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'back_2')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Выбирай на здоровье!", reply_markup=all_categories)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'pregnant_16')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Беременна в 16🤰 \n https://youtu.be/L24vSR6GfnU?si=xVwBsObytGEHuO-U" , reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'married')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Давай поженимся💍 \n https://youtu.be/hsoS-9wPlSY?si=2m_-PF8ouDJOwVrc", reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'lets_speak')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Пусть говорят🗣 \n https://youtu.be/s1tBO6l7szA?si=tuXNxkDEnCuqrG4a"  , reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'pacanki')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Пацанки🤷 \n https://youtu.be/hhJQMSRZtSY?si=mHe57RwKG88-HGoO"  , reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'betray')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Измены💁‍♂️ \n https://youtu.be/lN-94Z0tEZg?si=EL0GY1Vw8clzEu2E"  , reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'eat_choice')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    to_eat = random.choice(eat_list)
    to_drink = random.choice(drinks)
    await bot.send_animation(call.from_user.id, r'https://media.tenor.com/e7fGXwHc3G8AAAAC/чётожратьзахотелось-приятныйильдар.gif', caption=f"Предлагаю взять {to_eat} на похрумкать🍽 и {to_drink}🍹", reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'back_to_categories')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Выбирай на здоровье!", reply_markup=all_categories)
    await call.message.delete()
