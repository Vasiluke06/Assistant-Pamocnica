from aiogram import Bot, Dispatcher
from core.config import settings
from tg_bot.handlers.basic import router as basic_router

bot = Bot(token=settings.bot_token.get_secret_value())
dp = Dispatcher()

dp.include_router(basic_router)