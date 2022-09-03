# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = '''I have no idea wtf im doing'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, changeicon: str, url: str):
    """Changes the icon of the server"""
    with open(url, 'rb') as f:
        icon = f.read()
    await bot.edit_server(ctx.message.server, icon=icon)

bot.run(TOKEN)
