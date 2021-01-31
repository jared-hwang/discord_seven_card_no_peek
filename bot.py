import os, time
import discord
from discord.ext import commands
from card_game import *

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name='jacks')
async def jacks(ctx):
    await ctx.send("<:pokerjack:805277442394030090>")

game = Game()
@bot.command(name='seatme')
async def seat_player(ctx):
    result = game.seat_player(ctx.author.name)
    if result[0]:
        await ctx.send(f"Seated! Players: {', '.join(game.players)}") 
    else:
        await ctx.send(f"{result[1]}. Players: {', '.join(game.players)}") 

@bot.command(name='unseatme')
async def unseat_player(ctx):
    result = game.unseat_player(ctx.author.name)
    if result[0]:
        await ctx.send(f"Unseated! Players: {', '.join(game.players)}") 
    else:
        await ctx.send(f"{result[1]} Players: {', '.join(game.players)}") 

bot.run(TOKEN)
