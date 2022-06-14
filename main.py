from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.dispatcher.filters import Text
from tugmalar import config
from aiogram.types import Message
import sqlite3
from sqlite import Database
import asyncio
db=Database('main.db')

API_TOKEN = '5465689385:AAGrNuWtVCA95K203zsxoofahoPKVZJa08k'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    name=message.from_user.username
    try:
        db.create_table_users()
    except:
        pass
    #Foydalanuvchini  bazaga qoshimiz
    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name,
                    email=f"@{name}")
        count_user=db.count_users()[0]
        mes = f"Bazaga@{name} qoshildi. Bazada {count_user} foydalanuvchi"
        await bot.send_message(chat_id=599331, text=mes)
    except sqlite3.IntegrityError:
        pass
    await message.answer("Assalomu Alaykum, iltimos tilni tanlang"
                         "Здравствуйте, пожалуйста выберайте язык", reply_markup=config.kirish_qismi)

@dp.message_handler(user_id=599331, text="users") # foydalanuvchilar soni
async def allusers(message: Message):
    users=db.select_all_users()
    await message.answer(users)

@dp.message_handler(text="reklama", user_id=599331)  # reklama jonatish
async def send_ad_to_all(message: types.Message):
    rek_mes = message.reply_to_message.message_id
    n = 0
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.forward_message(chat_id=user_id, from_chat_id=599331, message_id=rek_mes)
            await asyncio.sleep(0.1)
            n += 1
        except:
            pass
    await message.answer(f"Ushbu xabar {n} ta foydalanuvchiga yetib bordi.")

@dp.message_handler(text="add", user_id=599331) # odam qoshish
async def add_us(mes: types.Message):
    id_name = list(mes.reply_to_message.text.split())
    id_raqam = int(id_name[0])
    name = id_name[1]
    if len(id_name) == 3:
        email = id_name[2]
    else:
        email = None

    try:
        db.add_user(id_raqam, name, email)
    except sqlite3.IntegrityError:
        pass
    await mes.answer(f"{id_raqam} raqamli {name} {email}")

@dp.message_handler(Text(equals="Orqaga"))
async def orqaga(message: types.Message):
    await message.answer("Bugungi taomnomada", reply_markup=config.kirish_qismi)

@dp.message_handler(Text(equals="O'zbekcha"))
async def til(message: types.Message):
    await message.answer("Bugungi taomnomada", reply_markup=config.asosiy_menu)

@dp.message_handler(Text(equals="Milliy taomlar retseptlari"))
async def mil_taom_ret(message:types.Message):
    await message.answer_video("https://t.me/oshxona_oshpaz_pazanda_retseptla/15916", reply_markup=config.Mil_taom_rets)

@dp.callback_query_handler(Text(equals="osh"))
async def oshpalov(call: CallbackQuery):
    await call.message.answer_video()




@dp.message_handler(commands=['yordam'])
async def yordam(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bu bot nimadir qilish uchun yordam beradi.")


# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer("Bunday  buyruq mavjudmas")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)