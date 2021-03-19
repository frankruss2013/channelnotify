from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import telegram
import time


def telegram_client(phone, api_id, api_hash):
    client = TelegramClient(phone, api_id, api_hash)
    time.sleep(3)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    return client


def targeted_channel():
    chats = []
    last_date = None
    chunk_size = 200
    channels = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == False:
                channels.append(chat)
        except:
            continue
    print('Choose a channel to scrap message:')
    i = 0
    for channel in channels:
        print(str(i) + '- ' + channel.title)
        i += 1

    c_index = input("Enter a Number: ")
    target_channel = channels[int(c_index)]
    return target_channel


def messages_from_channel(target_channel):
    messages = []
    for message in client.iter_messages(target_channel):
        messages.append(message.text)

    return messages
def get_message(offset=0, timeout=300):
    message_list = bot.get_updates(offset=offset, timeout=timeout)
    return message_list


if __name__ == "__main__":
    api_id = 1685820
    api_hash = '3a61416a9958dd57bba65545344ad42a'
    phone = '+919415222238'

    token = '1646681577:AAGdgFTPsRDmoQd49oaAHaN6j3Hx6G8xjo0'
    bot = telegram.Bot(token=token)

    client = telegram_client(phone, api_id, api_hash)
    channel_source = targeted_channel()
    total_post = len(messages_from_channel(channel_source))
    posts = messages_from_channel(channel_source)
    print('Checking for messages:')
    while True:
        posts = messages_from_channel(channel_source)
        total_post_updated = len(posts)
        if total_post_updated > total_post:
            total_post = total_post_updated
            if ('Binance' in posts[0])\
            and ('List' in posts[0])\
            and ('Innovation Zone' in posts[0]):
                bot.send_message(537873468, 'Notification')
                print('Notification Appears.')
