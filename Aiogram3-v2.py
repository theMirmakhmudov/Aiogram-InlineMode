import asyncio
import logging
from aiogram import Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import TOKEN
from aiogram import Bot
import hashlib

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}")


@dp.inline_query()
async def inline_query(query: types.InlineQuery):
    text = query.query
    result_id_tashkent = hashlib.md5(f"{text}_tashkent".encode()).hexdigest()
    result_id_namangan = hashlib.md5(f"{text}_namangan".encode()).hexdigest()

    locations = [
        types.InlineQueryResultLocation(
            id=result_id_tashkent,
            title="Toshkent",
            latitude=41.2995,
            longitude=69.2401,
            input_message_content=types.InputLocationMessageContent(
                latitude=41.2995,
                longitude=69.2401
            )
        ),
        types.InlineQueryResultLocation(
            id=result_id_namangan,
            title="Namangan",
            latitude=40.9983,
            longitude=71.6726,
            input_message_content=types.InputLocationMessageContent(
                latitude=40.9983,
                longitude=71.6726
            )
        )
    ]

    await query.answer(results=locations, cache_time=1, is_personal=True)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
