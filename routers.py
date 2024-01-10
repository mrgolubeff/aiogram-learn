from aiogram import Router, filters
from aiogram.filters import Command
from aiogram.types import Message

router1 = Router()
router2 = Router()


@router1.message(Command('router1'))
async def cmd_router1(m: Message):
    await m.answer(
        'Hello from router 1'
    )


@router2.message(Command('router2'))
async def cmd_router2(m: Message):
    await m.answer(
        'Hello from router 2'
    )
