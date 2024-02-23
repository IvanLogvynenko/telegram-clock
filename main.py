import time

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon import TelegramClient

from src.configuration import Configuration
from src.auth import auth
from src.ImageGenerator import ImageGenerator

import asyncio
import schedule


async def profile_photo_changer(client: TelegramClient):
    print("update")
    img_link = ImageGenerator.generate_clock_image()
    result = await client.upload_file(img_link)

    for photo in await client.get_profile_photos('me'):
        print(photo)
        await client(DeletePhotosRequest([photo]))

    await client(UploadProfilePhotoRequest(file=result))


async def main():
    conf = Configuration()
    client = await auth(conf)

    while True:
        current_time = time.time()
        next_minute = (int(current_time) // 60 + 1) * 60
        await asyncio.sleep(next_minute - current_time)
        await profile_photo_changer(client)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
