from telethon import TelegramClient, events, connection
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from config import api_id, api_hash, proxy_type, admins
from proxy_config import proxy
from telethon import errors as tel_errs
import asyncio
import logging

logging.basicConfig(level=logging.WARNING)

if proxy is None:
    client = TelegramClient('anon', api_id, api_hash)
elif proxy_type == 'MTProto':
    client = TelegramClient(
        'anon',
        api_id,
        api_hash,
        connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
        proxy=proxy
    )
else:
    client = TelegramClient('anon', api_id, api_hash, proxy=proxy)


with open('chats.txt', 'r') as chats_file:
    chats = chats_file.read().split('\n')
    chats = list(filter(lambda i: not i.startswith('#') and not i == '', chats))


@client.on(events.NewMessage(incoming=True, pattern=r'\/mailing', func=lambda m: m.reply_to_msg_id is not None and m.from_id in admins))
async def start_mailing(event):
    failed_chats = ''
    n = 0
    for chat in chats:
        try:
            if '/joinchat/' in chat:
                chat_hash = chat.split('/joinchat/')[1]
                await client(ImportChatInviteRequest(chat_hash))
            else:
                await client(JoinChannelRequest(chat))
        except tel_errs.UserAlreadyParticipantError:
            pass
        try:
            mailing_message = await event.message.get_reply_message()
            await client.send_message(chat, mailing_message)
        except Exception as e:
            print(chat+' '+str(e))
            failed_chats += chat + '\n'
        n += 1
        if n == 6:
            await asyncio.sleep(20)
            n = 0
    for admin in admins:
        try:
            await client.send_message(admin, 'Mailing is finished. Failed chats:\n{}'.format(failed_chats), link_preview=False)
        except:
            continue


client.start()
client.run_until_disconnected()
