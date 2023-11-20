from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


info = InlineKeyboardMarkup(row_width=1)

about_me = InlineKeyboardButton(text="Узнай обо мне", callback_data="about_me")
info.insert(about_me)
show_video = InlineKeyboardButton(text="Покажи видео", callback_data="video")
info.insert(show_video)
show_stickers = InlineKeyboardButton(text="Хочу стикеры", callback_data="sticker")
info.insert(show_stickers)


info_keyboard = InlineKeyboardMarkup(row_width=1)
about = InlineKeyboardButton(text="Немного обо мне",url="https://t.me/masterildar")
info_keyboard.insert(about)
social = InlineKeyboardButton(text="Мои соц.сети", url="https://t.me/masterildar")
info_keyboard.insert(social)
clothes = InlineKeyboardButton(text="Зацени мой новый мерч!", url="https://prostomerch.store/catalog/collections/priyatnyj-ildar")
info_keyboard.insert(clothes)
go_back = InlineKeyboardButton(text="Вернуться",callback_data="go_back")
info_keyboard.insert(go_back)


less_info = InlineKeyboardMarkup(row_width=1)
about = InlineKeyboardButton(text="Узнай обо мне", callback_data="about_me")
less_info.insert(about)
show_vid = InlineKeyboardButton(text="Покажи видео", callback_data="video")
less_info.insert(show_vid)


no_info = InlineKeyboardMarkup(row_width=1)
give_sticker = InlineKeyboardButton(text="Хочу стикеры", callback_data="sticker")
no_info.insert(give_sticker)
show_vid = InlineKeyboardButton(text="Покажи видео", callback_data="video")
no_info.insert(show_vid)

go_to_videos = InlineKeyboardMarkup(row_width=1)
categories = InlineKeyboardButton(text="Категории",callback_data="categories")
go_to_videos.insert(categories)
random = InlineKeyboardButton(text="Удиви меня!", url="https://www.youtube.com/watch?v=jMfrWa0wuTw&t=3s")
go_to_videos.insert(random)
background_video = InlineKeyboardButton(text="На фон", url="https://www.youtube.com/watch?v=jMfrWa0wuTw&t=3s")
go_to_videos.insert(background_video)
fresh_video = InlineKeyboardButton(text="Покажи свежак",url="https://www.youtube.com/watch?v=jMfrWa0wuTw&t=3s")
go_to_videos.insert(fresh_video)

all_categories = InlineKeyboardMarkup(row_width=1)
men_women = InlineKeyboardButton(text="Мужское/Женское",url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOnWdt5SbY0T-BeXfcWXbini")
all_categories.insert(men_women)
pregnant_16 = InlineKeyboardButton(text="Беременна в 16", url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOnXk0o6bV1Hco_Qz_mtnDF5")
all_categories.insert(pregnant_16)
married = InlineKeyboardButton(text="Давай поженимся", url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOkAQsQlMeS4Plsir7xgsgSN")
all_categories.insert(married)
lets_speak = InlineKeyboardButton(text="Пусть говорят",url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOmVIExI1q07ja2IWbWE92bq")
all_categories.insert(lets_speak)
pacanki = InlineKeyboardButton(text="Пацанки", url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOlyduaCaaljNLj6np5GpRix")
all_categories.insert(pacanki)
betray = InlineKeyboardButton(text="Измены", url="https://www.youtube.com/playlist?list=PL7-a4pKt1YOl1nv9qgyWsiIboxLr7KgUm")
all_categories.insert(betray)

