from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



kirish_qismi = ReplyKeyboardMarkup([
    [KeyboardButton("O'zbekcha"), KeyboardButton("Русский")],
    #[KeyboardButton("Geo-manzilni jonatish", request_location=True), KeyboardButton("Telefon raqam", request_contact=True)],
], resize_keyboard=True
)

asosiy_menu = ReplyKeyboardMarkup([
    [KeyboardButton("Milliy taomlar retseptlari"), KeyboardButton("Yevropa taomlari"), KeyboardButton("Uygur milliy taomlari")],
    [KeyboardButton("Shirinliklar"),KeyboardButton("Ichimliklar"), KeyboardButton("Orqaga")],
], resize_keyboard=True
)

# Mil_taom_rets = ReplyKeyboardMarkup([
#     [KeyboardButton("Osh"), KeyboardButton("Yevropa taomlari"), KeyboardButton("Uygur milliy taomlari")],
#     [KeyboardButton("Shirinliklar"),KeyboardButton("Ichimliklar"), KeyboardButton("Orqaga")],
# ], resize_keyboard=True
# )

Mil_taom_rets= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Osh", callback_data="osh"),
            InlineKeyboardButton(text="Dimlama", callback_data="dimlama"),
        ],
        [
            InlineKeyboardButton(text="Qozon kabob", callback_data="qozon_kabob"),
            InlineKeyboardButton(text="Dum kabob", callback_data="dum_kabob"),
        ],
        [
            InlineKeyboardButton(text="Xonim", callback_data="xonim"),
            InlineKeyboardButton(text="Manti", callback_data="manti"),
        ]

    ]
)