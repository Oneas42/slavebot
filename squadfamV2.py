# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='.')

@bot.command(name='..', help='A natural response')
async def quote(ctx):

    rsun_quote = [
        'wat', 'wtf gay', '???', 'bruh', 'kek',
        'hmmm', 'wtf', 'gay', 'cancer', 'cringe',
        'lel', 'kinda cringe', 'nibba', 'O',
        'play genshin impact', 'my dad beat me today', 'HaHa, You\'re Bad.', 'Haha, play Valorant you pussy.'
        ]

    response = random.choice(rsun_quote)
    await ctx.send(response)

@bot.command(name='roast', help='A savage roast')
async def roast(ctx):

    mmao_roast = [
    'no u', 'u dumb bitch',
    'your IQ is lower than room temperature', 'you\'re so full of shit, your eyes are brown',
    'at least I\'m not working a minimun wage job', 'stop inting', 'friggin\' python simp',
    'reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'stop counting with your fingers', 'you\'re so full of shit, the toilet\'s jealous',
    'at least I have rights', 'the custody battle will be for who doesn\'t have to take you',
    'you look like an unshaved testicle', 'I bet your brain feels good as new, seeing that you haven\'t used it',
    'I don\'t hate you, but I would unplug your life support to charge my phone', 'I postulate you suck'
    ]

    response = random.choice(mmao_roast)
    await ctx.send(response)

@bot.command(name='whitebag', help='What white bag will you get?')
async def sad(ctx):

    white_bag = [
    'Divinity', 'Oryx\'s Escutcheon', 'Gladiator Guard', 'Exalted God\'s Horn',
    'Enforcer', 'Ballistic Star', 'Centaur\'s Shielding', 'Battalion Banner',
    'Lumiaire', 'Chaotic Scripture', 'Vesture of Duality', 'Divine Coronation',
    'Avarice', 'Gambler\'s Fate', 'Turncoat Cape', 'Collector\'s Monocle',
    'Superior', 'Genesis Spell', 'Diplomatic Robe', 'Chancellor\'s Cranium',
    ]

    response = random.choice(white_bag)
    await ctx.send(response)

@bot.command(name='rock', help='Pick rock in a round of RPS')
async def rps(ctx):

    rpsi = ['rock', 'paper', "scissor"]

    response = random.choice(rpsi)
    await ctx.send(response)
    if response == 'rock':
        await ctx.send('Issa tie!')
    elif response == 'paper':
        await ctx.send('HaHa, You lose.')
    else:
        await ctx.send('GG You Win!')

@bot.command(name='paper', help='Pick paper in a round of RPS')
async def rps(ctx):

    rpsi = ['rock', 'paper', "scissor"]

    response = random.choice(rpsi)
    await ctx.send(response)
    if response == 'rock':
        await ctx.send('GG You Win!')
    elif response == 'paper':
        await ctx.send('Issa tie!')
    else:
        await ctx.send('HaHa, You lose.')

@bot.command(name='scissor', help='Pick scissor in a round of RPS')
async def rps(ctx):

    rpsi = ['rock', 'paper', "scissor"]

    response = random.choice(rpsi)
    await ctx.send(response)
    if response == 'rock':
        await ctx.send('HaHa, You lose.')
    elif response == 'paper':
        await ctx.send('GG You Win!')
    else:
        await ctx.send('Issa tie!')

@bot.command(name='potato', help='Summons a potato')
async def tits(ctx):

    potato_image = [
    'Potatoes\\potato1.png', 'Potatoes\\potato1.jpg'
    ]

    await ctx.send(
        file=discord.File(random.choice(potato_image))
    )

@bot.command(name='dice', help='Roll a dice')
async def roll(ctx):
    dice = [
        str(random.choice(range(1, 6)))
    ]
    await ctx.send(', '.join(dice))

@bot.command(help='\"Repeat after me\"')
async def repeat(ctx, *, arg):
    await ctx.send(arg)

@bot.command(name='create', help='Create a Character')
async def create_char(ctx):
    char_hp = random.choice(range(1,6))
    char_atk = random.choice(range(1,6))
    char_def = random.choice(range(1,6))
    char_spd = random.choice(range(1,6))
    char_rcv = random.choice(range(1,6))

    char_tot_stats = char_hp + char_atk + char_def + char_spd + char_rcv
    while char_tot_stats < 15:
        if char_tot_stats >= 15:
            break
    await ctx.send(
        'HP: ' + str(char_hp + 6) +
        '\nAtk: ' + str(char_atk) + '\tDef: ' + str(char_def) +
        '\nSpd: ' + str(char_spd) + '\tRCV: ' + str(char_rcv)
    )

bot.run(TOKEN)
