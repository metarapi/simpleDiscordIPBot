
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#0: Load token from somewhere safe
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

#1: Bot setup. Intents are required to access certain events
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

#2: Bot event handlers
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled)')
        return
    
    is_private = user_message[0] == '?'

    if is_private:
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#3: Handling bot startup
@client.event
async def on_ready():
    print(f'{client.user} is running!')

#4: Handling messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str( message.channel)

    print(f'[{username}] {channel}: {user_message}')
    await send_message(message, user_message)

#5: Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()