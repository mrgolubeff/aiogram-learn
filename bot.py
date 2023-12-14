import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
token = ""
with open('bot.config') as f:
    token = f.readline()
    token = token.replace("\n", "")
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply("Это реплай")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.message.register(cmd_test2, Command("test2"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
