import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton,ContentType

from handlers.users.eat_choice import eat_list, drinks
from keyboards.inline.choice_buttons import info, info_keyboard, all_categories, go_to_videos, eat, end, after_pregnant_16
from handlers.users.videos_links import men_women, pregnant_16
from loader import dp, bot

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.message_handler(Command("start"))
async def cmd_start(message: Message):
    await bot.send_animation(message.from_user.id, r'https://media.tenor.com/9gNWL-w1CiQAAAAC/иэтонешутка-its-not-a-joke.gif', caption="Доброго времени суток, мой приятный друг, рад тебя видеть!💗 Нажми, что хочешь сделать👇", reply_markup=info)
    await message.delete()

@dp.message_handler()
async def echo(message:Message):
    await bot.send_animation(message.from_user.id,r'https://media.tenor.com/y7ym4Yrdm98AAAAC/кричать-обоже.gif',caption="Я не против пообщаться, но лучше потыкай по кнопочкам🙃", reply_markup=info)


@dp.message_handler(content_types=ContentType.STICKER)
async def handle_sticker(message:Message):
    await bot.send_animation(message.from_user.id,r'https://media.tenor.com/AN9twiCPQg8AAAAC/огоого-oh-oh.gif', caption="Бомбовый стикер, дружище🫡\n Но с кнопками проще)", reply_markup=info)





@dp.callback_query_handler(lambda c: c.data == 'about_me')
async def showing_info(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await call.message.answer("Мне приятно, что ты хочешь узнать обо мне побольше. Здесь ты сможешь найти ссылки на мои соц.сети и сайт с уникальным мерчем 😎",
                              reply_markup=info_keyboard)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'sticker')
async def process_callback_button3(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(callback_query.from_user.id, sticker="CAACAgIAAxkBAAEK22llaHpdvTTRqFRdI-niaEotEgMV7QACGToAAoj-MUs6HBvpS7CmzzME")
    await bot.send_message(callback_query.from_user.id, text="Забирай мой новый стикерпак 👉 и возвращайся🫶", reply_markup=do_back())
    await callback_query.message.delete()
def do_back():
    back_button = InlineKeyboardMarkup().add(InlineKeyboardButton("Вернуться🔙", callback_data="back"))
    return back_button


@dp.callback_query_handler(lambda c: c.data == 'back')
async def call_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Что делать будем?", reply_markup=info)
    await call.message.delete()



@dp.callback_query_handler(lambda c: c.data == 'go_back')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Что делать будем?", reply_markup=info)
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
    link = random.choice(men_women)
    await bot.send_message(call.from_user.id, f"Лови видео по категории Мужское/Женское👫 \n {link}", reply_markup=eat)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'back_2')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Выбирай на здоровье!", reply_markup=all_categories)



@dp.callback_query_handler(lambda c: c.data == 'pregnant_16')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    link = random.choice(pregnant_16)
    await bot.send_message(call.from_user.id, f"Лови видео по категории Беременна в 16🤰 \n {link}" , reply_markup=after_pregnant_16)
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


@dp.callback_query_handler(lambda c: c.data == 'back_to_info')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Что делать будем?", reply_markup=info)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'more')
async def more(call:CallbackQuery):
    new_link = random.choice(men_women)
    await bot.send_message(call.from_user.id, f"Лови еще видео по категории Мужское/Женское👫 \n {new_link}", reply_markup=eat)


@dp.callback_query_handler(lambda c: c.data == 'more_2')
async def more2(call:CallbackQuery):
    if pregnant_16:
        new_link_16 = random.choice(pregnant_16)
        pregnant_16.remove(new_link_16)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Беременна в 16🤰  \n {new_link_16}",
                               reply_markup=after_pregnant_16)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)

@dp.callback_query_handler(lambda c: c.data == 'prediction')
async def send_prediction(callback_query: CallbackQuery):
    predictions = ["Красивый, умный и любящий человек войдет в вашу жизнь.", "Ваша жизнь будет счастливой и мирной.", "Хорошие вещи придут к вам."]
    prediction = random.choice(predictions)
    await bot.send_message(callback_query.from_user.id, prediction, reply_markup=do_back())
def do_back():
    back_button = InlineKeyboardMarkup().add(InlineKeyboardButton("Вернуться🔙", callback_data="back"))
    return back_button




