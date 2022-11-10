from aiogram import Bot, Dispatcher,types,executor
import logging
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import bold
import sqlite3
from sqlite3 import Error



def sql_connection():
	try:
		con = sqlite3.connect('mdatabase.db')
		return con
	except Error:
		print(Error)
	
def sql_table(con):
	cursorObj = con.cursor()
	cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(name TEXT, age INT)")
	con.commit()

def sql_insert(con):
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO employees VALUES('Tolik', 37)")
	con.commit()

def sql_update(con):
	cursorObj = con.cursor()
	cursorObj.execute('UPDATE employees SET name = "Anatoliy" WHERE age = 37 ')
	con.commit()

def sql_fetch(con):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT age from employees')
	a = (cursorObj.fetchall())
	return a
	
token = '5659473142:AAHNsnHfaM6Dna6rcgFm85xU90h0v0H-NiA'
bot = Bot(token=token)
dp = Dispatcher(bot)
con = sql_connection()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	button_box = ['Создать и подключить','Добавить','Показать']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*button_box)
	await message.answer('Ок', reply_markup=keyboard)

@dp.message_handler(Text(equals='Создать и подключить'))
async def marks(message: types.Message):
	await message.answer('Секундочку...')
	sql_table(con)
	await message.answer('Ок',parse_mode= "Markdown")
	
@dp.message_handler(Text(equals='Добавить'))
async def marks(message: types.Message):
	await message.answer('Секундочку...')
	sql_insert(con)
	await message.answer(2,parse_mode= "Markdown")
	await message.answer(3,parse_mode= "Markdown")

@dp.message_handler(Text(equals='Показать'))
async def marks(message: types.Message):
	b = sql_fetch(con)
	
	await message.answer(b,parse_mode= "Markdown")
	
	
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
