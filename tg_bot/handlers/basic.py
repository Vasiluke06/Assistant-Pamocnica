from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Hello! You're in the chat of Pamocnica Assistant and I'm your assistant. Feel free to ask questions"
    )