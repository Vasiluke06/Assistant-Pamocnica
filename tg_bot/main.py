import asyncio
import logging
from tg_bot.bot_instance import bot, dp

logging.basicConfig(level=logging.INFO)

async def main():
    logging.info("Telegram bot activation")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())