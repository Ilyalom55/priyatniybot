from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


info = InlineKeyboardMarkup(row_width=1)

about_me = InlineKeyboardButton(text="Узнай обо мне", callback_data="about_me")
info.insert(about_me)
show_video = InlineKeyboardButton(text="Покажи видео", callback_data="video")
info.insert(show_video)
show_stickers = InlineKeyboardButton(text="Хочу стикеры", callback_data="sticker")
info.insert(show_stickers)


info_keyboard = InlineKeyboardMarkup(row_width=1)
about = InlineKeyboardButton(text="Мой инстаграм",url="instagram.com/masterildar")
info_keyboard.insert(about)
social = InlineKeyboardButton(text="Телеграм-канал", url="https://t.me/masterildar")
info_keyboard.insert(social)
vk = InlineKeyboardButton(text="Сообщество Вконтакте", url="vk.com/pleasentildar")
info_keyboard.insert(vk)
clothes = InlineKeyboardButton(text="Зацени мой мерч!", url="https://prostomerch.store/catalog/collections/priyatnyj-ildar")
info_keyboard.insert(clothes)
go_back = InlineKeyboardButton(text="Вернуться🔙",callback_data="go_back")
info_keyboard.insert(go_back)


less_info = InlineKeyboardMarkup(row_width=1)
about = InlineKeyboardButton(text="Узнай обо мне😏", callback_data="about_me")
less_info.insert(about)
show_vid = InlineKeyboardButton(text="Покажи видео🎬", callback_data="video")
less_info.insert(show_vid)


no_info = InlineKeyboardMarkup(row_width=1)
give_sticker = InlineKeyboardButton(text="Хочу стикеры😍", callback_data="sticker")
no_info.insert(give_sticker)
show_vid = InlineKeyboardButton(text="Покажи видео🎬", callback_data="video")
no_info.insert(show_vid)

go_to_videos = InlineKeyboardMarkup(row_width=1)
categories = InlineKeyboardButton(text="Категории🔝",callback_data="categories")
go_to_videos.insert(categories)
playlists = InlineKeyboardButton(text="К плейлистам👉", url="https://www.youtube.com/@pleasantildar/playlists")
go_to_videos.insert(playlists)
random = InlineKeyboardButton(text="Рандомный кайф🎰", url="https://www.youtube.com/watch?v=jMfrWa0wuTw&t=3s")
go_to_videos.insert(random)
background_video = InlineKeyboardButton(text="Послушать на фон🔈", url="https://www.youtube.com/watch?v=jMfrWa0wuTw&t=3s")
go_to_videos.insert(background_video)
fresh_video = InlineKeyboardButton(text="Покажи свежак🆕",url="https://youtu.be/gASBs8pRtLU?si=jKcHsgOmGvFqUt-q")
go_to_videos.insert(fresh_video)

all_categories = InlineKeyboardMarkup(row_width=1)
#men_women = InlineKeyboardButton(text="Мужское/Женское",url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOnWdt5SbY0T-BeXfcWXbini")
#all_categories.insert(men_women)
men_women = InlineKeyboardButton(text="Мужское/Женское👫",callback_data="men_women")
all_categories.insert(men_women)
pregnant_16 = InlineKeyboardButton(text="Беременна в 16🤰", callback_data="pregnant_16")
all_categories.insert(pregnant_16)
married = InlineKeyboardButton(text="Давай поженимся💍", callback_data="married")
all_categories.insert(married)
lets_speak = InlineKeyboardButton(text="Пусть говорят🗣",callback_data="lets_speak")
all_categories.insert(lets_speak)
pacanki = InlineKeyboardButton(text="Пацанки🤷", callback_data="pacanki")
all_categories.insert(pacanki)
betray = InlineKeyboardButton(text="Измены💁‍♂️", callback_data="betray")
all_categories.insert(betray)
back = InlineKeyboardButton(text="Назад🔙", callback_data="back_to_choice")
all_categories.insert(back)



eat = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Назад🔙", callback_data="back_2")
eat.insert(back_2)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
eat.insert(choice)


end = InlineKeyboardMarkup(row_width=1)
back_to_categories = InlineKeyboardButton(text="Назад🔙", callback_data="back_to_categories")
end.insert(back_to_categories)
