import logging

from PIL import Image
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart

API_TOKEN = '5677558917:AAFLDX-FHia83vuONJAYMEggrz1mJT5aIZU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    file_id = message.photo[0].file_id
    i = Image.open(await bot.download_file_by_id(file_id))
    await message.answer_photo(message.photo[0].file_id, "caption")
    # await bot.send_photo(message.from_user.id, message.photo[0].file_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
