from telethon import TelegramClient

from src.configuration import Configuration


async def auth(conf) -> TelegramClient:
    client = TelegramClient(conf.SESSION_NAME, conf.API_ID, conf.API_HASH)
    await client.start()
    print("Starting Telegram client")
    await client.sign_in()
    print("Logged in")

    return client
