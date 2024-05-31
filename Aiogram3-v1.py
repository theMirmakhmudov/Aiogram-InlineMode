import asyncio
import logging
from aiogram import Dispatcher, F, types
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
async def inline_query_message(query: types.InlineQuery):
    if query.query == "data":
        text = query.query
        link = "http://127.0.0.1:8000"  # Tuple emas, faqat satr
        result_id = hashlib.md5(text.encode()).hexdigest()

        articles = [types.InlineQueryResultArticle(
            id=result_id,
            title="Examte test rejim",
            url=link,
            input_message_content=types.InputTextMessageContent(message_text=link)
        )]

        await query.answer(results=articles, cache_time=1, is_personal=True)

    elif query.query == "images":
        text = query.query
        link = "http://127.0.0.1:8000/images"
        result_id = hashlib.md5(text.encode()).hexdigest()

        photos = [types.InlineQueryResultPhoto(
            id=result_id,
            title="Example photo",
            photo_url="https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
            photo_width=100,
            photo_height=100,
            thumbnail_url=link,
            caption="Example Photode"
        )]

        await query.answer(results=photos, cache_time=1, is_personal=True)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
