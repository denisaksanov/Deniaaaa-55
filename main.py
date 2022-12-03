#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token="5640502690:AAGHE6yMY1fRcGmFw2YyR8YreaoqHbt7t1M")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения


# Хэндлер на команду /test1
@dp.message_handler(commands="Привет")
async def cmd_test1(message: types.Message):
    await message.reply("салам")
#таким образом мы придумываем команду
@dp.message_handler(commands="getPos")
# любая функция с названием
async def cmd_getPos(message: types.Message):
    # вся работа весь код в дальнейшем
    await message.reply('Будущая команда пока в разработке')
#создаем переменную
i = 777877
@dp.message_handler()
async def cmd_text(message: types.Message):

    if message.text == "привет":
        await  bot.send_message(message.from_user.id, "салам")
    #elif добавление новой команды
    elif message.text == "Привет":
        await  bot.send_message(message.from_user.id, "Дарова")
    elif message.text == "test1":
        await  bot.send_message(message.from_user.id, 'hi')
    elif message.text == "Умножить":
        #делаем переменную глобальной для обращения к нему
        global i
        i = i * 2
        await bot.send_message(message.from_user.id, str(i))
    elif message.text == "Отнять":
        i = i - 2
        await bot.send_message(message.from_user.id, str(i))
    #проверить что слово есть в сообщении
    elif "прибавить" in message.text:
        i = i + 2
        await bot.send_message(message.from_user.id, str(i))
    # ЭТО САМАЯ ПОСЛЕДНЯЯ КОМАНДА ВСЕГДА
    else:
        await  bot.send_message(message.from_user.id, "Не знаю , что на это ответить")



if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp)

