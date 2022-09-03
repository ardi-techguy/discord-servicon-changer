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

@client.command()
async def add(ctx, changeicon: str, url: str):
    """Changes the icon of the server"""
    with open(url, 'rb') as f:
        icon = f.read()
    await bot.edit_server(ctx.message.server, icon=icon)

client.run(TOKEN)
