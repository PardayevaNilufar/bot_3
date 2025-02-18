from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from keyboards.inline.menu import kurslar,menu_start
from loader import dp,bot


#biz haqimizda tugmasi uchun handler
@dp.callback_query_handler(text="about")
async def about_page(call:types.CallbackQuery):
    text="""bizning o'quv markaz 
          IT ning barcha yo'nalishlarini qamrab oladi
    """
    await call.message.edit_text(text,reply_markup=menu_start,parse_mode="Markdown")




#aloqa tugmasi uchun handler
@dp.callback_query_handler(text="contact")
async def contact_page(call:types.CallbackQuery):
    text1=""" bizning telefon raqamimiz: +998 98 345 22 33
            bizning email pochtamiz:ardayevan88gmail,com
            bizning 24/7 ishlaymiz"""

    await call.message.edit_text(text1,reply_markup=menu_start,parse_mode="Markdown")


#yangilik uchun handler
@dp.callback_query_handler(text="news")
async def news_page(call:types.CallbackQuery):
    text2=""" bizda katta chegirmalar 
            ramozon oyi uchun 10
            toliq tolov uchun 15
            bizda yana yangi kurs ochilmoqda
            10-fevraldan backend va savodxonlik kursi uchun"""
    await call.message.edit_text(text2,reply_markup=menu_start,parse_mode="Markdown")


#mavjud kurslar uchun handler
@dp.callback_query_handler(text="courses")
async def courses_page(call:types.CallbackQuery):
    await call.message.edit_text("bizda mavjud kurslar",reply_markup=kurslar)




