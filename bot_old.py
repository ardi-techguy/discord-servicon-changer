# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    with open('image.jpg', 'rb') as f:
        icon = f.read()
    await client.edit_server(ctx.message.server, icon=icon)
    

client.run(TOKEN)
