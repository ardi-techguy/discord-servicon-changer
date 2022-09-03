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
async def changeicon(ctx):
    """Changes the icon of the server"""
    with open("image.png", 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)

bot.run(TOKEN)
