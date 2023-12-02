import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton,ContentType

from handlers.users.eat_choice import eat_list, drinks
from keyboards.inline.choice_buttons import info, info_keyboard, go_to_videos, all_categories, men_woman_kb, married_kb, pregnant_16_kb, lets_speak_kb, pacanki_kb, betray_kb, end, playlists_kb,random_kb, fresh_kb,prediction_kb
from handlers.users.videos_links import men_women_links, pregnant_16, married, lets_speak, pacanki, betray, randomize
from handlers.users.predictions import pechenie
from loader import dp, bot


@dp.message_handler(Command("start"))
async def cmd_start(message: Message):
    await bot.send_animation(message.from_user.id, r'https://media.tenor.com/9gNWL-w1CiQAAAAC/иэтонешутка-its-not-a-joke.gif', caption="Доброго времени суток, мой приятный друг, рад тебя видеть!💗 Нажми, что хочешь сделать👇", reply_markup=info)
    await message.delete()

@dp.message_handler()
async def echo(message:Message):
    await bot.send_animation(message.from_user.id,r'https://media.tenor.com/y7ym4Yrdm98AAAAC/кричать-обоже.gif',caption="Я не против пообщаться, но лучше потыкай по кнопочкам🙃", reply_markup=info)


@dp.message_handler(content_types=ContentType.STICKER)
async def handle_sticker(message:Message):
    await bot.send_animation(message.from_user.id,r'https://media.tenor.com/kUSm6DTcCMgAAAAC/смеяться-улыбаться.gif', caption="Бомбовый стикер, дружище🫡\n Но с кнопками проще)", reply_markup=info)


@dp.callback_query_handler(lambda c: c.data == 'about_me')
async def showing_info(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id, r'https://media.tenor.com/aT_EFA_1seUAAAAC/ода-oh-yeah.gif',caption= "Мне приятно, что ты хочешь узнать обо мне побольше❤️‍🔥\n Здесь ты сможешь найти ссылки на мои соц.сети и сайт с уникальным мерчем 😎",
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
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/sAcbZVKCdEMAAAAC/каквсегдасвами-приятныйильдар.gif',caption= "Продолжаем работать💪\n ", reply_markup=info)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'video')
async def go_to_video(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/-tc-RwryAFwAAAAM/нуиконечносамоеглавное-приятныйильдар.gif',caption= "Жмякай на кнопки👇, ну а я помогу с выбором🤗 ", reply_markup=go_to_videos)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'categories')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/z1djjf3TUyUAAAAC/мммдаженезнаю-приятныйильдар.gif',caption= "Выбирай на здоровье!", reply_markup=all_categories)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'back_to_choice')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/z1djjf3TUyUAAAAC/мммдаженезнаю-приятныйильдар.gif',caption= "Выбирай на здоровье!", reply_markup=go_to_videos)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'random')
async def random_choice(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    link = random.choice(randomize)
    await bot.send_message(call.from_user.id, f"Ну тут я взял на себя ответственность😉, принимай ссылку и наслаждайся🥳  \n {link}", reply_markup=random_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'men_women')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    link = random.choice(men_women_links)
    await bot.send_message(call.from_user.id, f"Вот тебе видосик по категории Мужское/Женское👫, наслаждайся🥳  \n {link}", reply_markup=men_woman_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'pregnant_16')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    link = random.choice(pregnant_16)
    await bot.send_message(call.from_user.id, f"Лови видео по категории Беременна в 16🤰и кайфуй💆 \n {link}" , reply_markup=pregnant_16_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'married')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Давай поженимся💍, уверен, тебе понравится😏\n https://youtu.be/iPQLZZeuecY?si=bHJw688o4buDljlR", reply_markup=married_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'lets_speak')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Пусть говорят🗣 и кайфуй💆 \n https://youtu.be/s1tBO6l7szA?si=tuXNxkDEnCuqrG4a"  , reply_markup=lets_speak_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'pacanki')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Лови видео по категории Пацанки🤷,уверен, тебе понравится\n https://youtu.be/hhJQMSRZtSY?si=mHe57RwKG88-HGoO"  , reply_markup=pacanki_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'betray')
async def go_to_categories(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Заводи кринжалёт и запускай видео по категории Измены💁‍♂️ \n https://youtu.be/lN-94Z0tEZg?si=EL0GY1Vw8clzEu2E"  , reply_markup=betray_kb)
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
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/z1djjf3TUyUAAAAC/мммдаженезнаю-приятныйильдар.gif',caption= "Выбирай на здоровье!", reply_markup=all_categories)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'categories_back')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/z1djjf3TUyUAAAAC/мммдаженезнаю-приятныйильдар.gif',caption= "Выбирай на здоровье!", reply_markup=all_categories)



@dp.callback_query_handler(lambda c: c.data == 'playlists')
async def playlists(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/AN9twiCPQg8AAAAC/огоого-oh-oh.gif',caption= "Вижу, у нас здесь самостоятельный человечек🫶\n Принимай ссылку на мои плейлисты!\n https://www.youtube.com/@pleasantildar/playlists", reply_markup=playlists_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'fresh')
async def playlists(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, "Самое свеженькое🔥\n Забирай ссылочку и переходи к просмотру💕 https://youtu.be/gASBs8pRtLU?si=3euyGG0S2JtEot39", reply_markup=fresh_kb)
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'back_to')
async def back_to_mess(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/z1djjf3TUyUAAAAC/мммдаженезнаю-приятныйильдар.gif',caption= "Выбирай на здоровье!", reply_markup=go_to_videos)


@dp.callback_query_handler(lambda c: c.data == 'more')
async def more(call:CallbackQuery):
    if men_women_links:
        new_link = random.choice(men_women_links)
        men_women_links.remove(new_link)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Мужское/Женское👫 \n {new_link}",
                               reply_markup=men_woman_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'more_2')
async def more2(call:CallbackQuery):
    if pregnant_16:
        new_link_16 = random.choice(pregnant_16)
        pregnant_16.remove(new_link_16)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Беременна в 16🤰  \n {new_link_16}",
                               reply_markup=pregnant_16_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'more_3')
async def more3(call:CallbackQuery):
    if married:
        new_link = random.choice(married)
        married.remove(new_link)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Давай поженимся💍  \n {new_link}",
                               reply_markup=married_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'more_4')
async def more2(call:CallbackQuery):
    if lets_speak:
        new_link = random.choice(lets_speak)
        lets_speak.remove(new_link)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Пусть говорят🗣 \n {new_link}",
                               reply_markup=lets_speak_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'more_5')
async def more2(call:CallbackQuery):
    if pacanki:
        new_link = random.choice(pacanki)
        pacanki.remove(new_link)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Пацанки🤷  \n {new_link}",
                               reply_markup=pacanki_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'more_6')
async def more2(call:CallbackQuery):
    if betray:
        new_link = random.choice(betray)
        betray.remove(new_link)
        await bot.send_message(call.from_user.id, f"Лови еще видео по категории Измены💁‍♂️  \n {new_link}",
                               reply_markup=betray_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'more_7')
async def more2(call:CallbackQuery):
    if randomize:
        new_link = random.choice(randomize)
        randomize.remove(new_link)
        await bot.send_message(call.from_user.id, f"Принимай новое видео и переходи к просмотру😇  \n {new_link}",
                               reply_markup=random_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="Сорри, но это все, чем я располагаю по выбранной категории😶‍🌫️",
                               reply_markup=end)


@dp.callback_query_handler(lambda c: c.data == 'prediction')
async def send_prediction(call: CallbackQuery):
    if pechenie:
        new_prediction = random.choice(pechenie)
        pechenie.remove(new_prediction)
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/BL92yB3_PaYAAAAC/дерзай-приятныйильдар.gif', caption=f"Вот твое предсказание:\n{new_prediction}" ,  reply_markup=prediction_kb)
    else:
        await bot.send_animation(call.from_user.id, r'https://media.tenor.com/oDOxbExCNqQAAAAC/скажучестно-i-will-be-honest.gif',caption="На этом мои полномочия все, я же не гадалка‍😶‍🌫️",
                               reply_markup=prediction_kb)

@dp.callback_query_handler(lambda c: c.data == 'back_to_start')
async def call_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_animation(call.from_user.id,r'https://media.tenor.com/sAcbZVKCdEMAAAAC/каквсегдасвами-приятныйильдар.gif',caption= "Продолжаем работать💪\n ", reply_markup=info)
    await call.message.delete()