from aiogram .types import InlineKeyboardMarkup, InlineKeyboardButton



menu_start=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⏰Mavjud kurslar",callback_data="courses"),
            InlineKeyboardButton(text="🔎biz haqimizda",callback_data="about"),
        ],
        [
            InlineKeyboardButton(text="📞Aloqa",callback_data="contact"),
            InlineKeyboardButton(text="🌎Manzil",callback_data="location"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻Royxatdan o'tish",callback_data="register"),
            InlineKeyboardButton(text="🖥️Yangiliklar",callback_data="news"),
        ],
        [
            InlineKeyboardButton(text="Takliflar",callback_data="feedback"),
        ],
    ]
)

kurslar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="backend dasturlash", callback_data="backend"),
        ],
        [
            InlineKeyboardButton(text="Frontend dasturlash", callback_data="frontend"),
        ],
        [
            InlineKeyboardButton(text="SMM", callback_data="smm"),
        ],
        [
            InlineKeyboardButton(text="Grafik dizayn", callback_data="grafik"),
        ],
        [
            InlineKeyboardButton(text="Kompyuter savodxonligi", callback_data="kompyuter"),
        ],

    ]
)