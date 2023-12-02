from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


info = InlineKeyboardMarkup(row_width=1)

about_me = InlineKeyboardButton(text="Расскажи о себе🤗", callback_data="about_me")
info.insert(about_me)
show_video = InlineKeyboardButton(text="Покажи видео🎬", callback_data="video")
info.insert(show_video)
show_stickers = InlineKeyboardButton(text="Подари мне стикеры😍", callback_data="sticker")
info.insert(show_stickers)
take_prediction = InlineKeyboardButton(text="Открой печеньку с предсказанием🍀", callback_data="prediction")
info.insert(take_prediction)

info_keyboard = InlineKeyboardMarkup(row_width=1)
my_site = InlineKeyboardButton(text="Обо мне🤗", url="https://dima731515.github.io/hakaton/html/index.html")
info_keyboard.insert(my_site)
about = InlineKeyboardButton(text="Мой инстаграм🫣",url="instagram.com/masterildar")
info_keyboard.insert(about)
social = InlineKeyboardButton(text="Телеграм-канал😻", url="https://t.me/unpleasent")
info_keyboard.insert(social)
vk = InlineKeyboardButton(text="Сообщество Вконтакте😋", url="vk.com/pleasentildar")
info_keyboard.insert(vk)
clothes = InlineKeyboardButton(text="Зацени мой мерч!🥷", url="https://prostomerch.store/catalog/collections/priyatnyj-ildar")
info_keyboard.insert(clothes)
go_back = InlineKeyboardButton(text="Вернуться🔙",callback_data="back")
info_keyboard.insert(go_back)


go_to_videos = InlineKeyboardMarkup(row_width=1)
categories = InlineKeyboardButton(text="Категории🔝",callback_data="categories")
go_to_videos.insert(categories)
playlists = InlineKeyboardButton(text="К плейлистам👉", callback_data="playlists")
go_to_videos.insert(playlists)
background_video = InlineKeyboardButton(text="Послушать на фон🔈", callback_data="random")
go_to_videos.insert(background_video)
fresh_video = InlineKeyboardButton(text="Покажи свежак🆕", callback_data="fresh")
go_to_videos.insert(fresh_video)
back = InlineKeyboardButton(text="Вернуться🔙", callback_data="back")
go_to_videos.insert(back)

playlists_kb = InlineKeyboardMarkup(row_width=1)
back = InlineKeyboardButton(text="Вернуться🔙", callback_data="back_to_choice")
playlists_kb.insert(back)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
playlists_kb.insert(choice)


all_categories = InlineKeyboardMarkup(row_width=1)
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
back = InlineKeyboardButton(text="Вернуться🔙", callback_data="back_to_choice")
all_categories.insert(back)


men_woman_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="categories_back")
men_woman_kb.insert(back_2)
more = InlineKeyboardButton(text="Другое видео", callback_data="more")
men_woman_kb.insert(more)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
men_woman_kb.insert(choice)


pregnant_16_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="categories_back")
pregnant_16_kb.insert(back_2)
more_2 = InlineKeyboardButton(text="Другое видео", callback_data="more_2")
pregnant_16_kb.insert(more_2)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
pregnant_16_kb.insert(choice)

married_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="categories_back")
married_kb.insert(back_2)
more_3 = InlineKeyboardButton(text="Другое видео", callback_data="more_3")
married_kb.insert(more_3)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
married_kb.insert(choice)

lets_speak_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="categories_back")
lets_speak_kb.insert(back_2)
more_4 = InlineKeyboardButton(text="Другое видео", callback_data="more_4")
lets_speak_kb.insert(more_4)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
lets_speak_kb.insert(choice)


pacanki_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="categories_back")
pacanki_kb.insert(back_2)
more_5 = InlineKeyboardButton(text="Другое видео", callback_data="more_5")
pacanki_kb.insert(more_5)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
pacanki_kb.insert(choice)


betray_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="categories_back")
betray_kb.insert(back_2)
more_6 = InlineKeyboardButton(text="Другое видео", callback_data="more_6")
betray_kb.insert(more_6)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
betray_kb.insert(choice)


random_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="back_to")
random_kb.insert(back_2)
more_7 = InlineKeyboardButton(text="Другое видео", callback_data="more_7")
random_kb.insert(more_7)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
random_kb.insert(choice)


fresh_kb = InlineKeyboardMarkup(row_width=1)
back_2 = InlineKeyboardButton(text="Вернуться🔙", callback_data="back_to")
fresh_kb.insert(back_2)
choice = InlineKeyboardButton(text="Подбери мне закусочку!", callback_data="eat_choice")
fresh_kb.insert(choice)


end = InlineKeyboardMarkup(row_width=1)
back_to_categories = InlineKeyboardButton(text="Назад🔙", callback_data="back_to_categories")
end.insert(back_to_categories)


prediction_kb = InlineKeyboardMarkup(row_width=1)
back_b = InlineKeyboardButton(text="Вернуться🔙", callback_data="back_to_start")
prediction_kb.insert(back_b)

