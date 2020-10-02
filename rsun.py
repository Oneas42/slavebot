# bot.py

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    rsun_quote = [
        'HaHa, You\'re Bad.', 'wat', 'wtf gay', '???', 'hmmm', 'wtf', 'gay', 'cancer', 'cringe', 'lol', 'lel', 'lul', 'kinda cringe', 'play genshin impact', 'my dad beat me today', 'bruh' ]

    if message.content == '.':
        response = random.choice(rsun_quote)
        await message.channel.send(response)

client.run(TOKEN)
