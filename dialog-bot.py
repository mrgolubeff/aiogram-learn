import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from config_reader import config

from aiogram_dialog import Window, Dialog, setup_dialogs, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Хранилище данных
storage = MemoryStorage()
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher(storage=storage)


class MySG(StatesGroup):
    main = State()

main_window = Window(
    Const("Hi, mom!"),
    Button(Const("Useless button"), id="nothing"),
    state=MySG.main,
)

dialog = Dialog(main_window)

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("dialog"))
async def cmd_dialog(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
