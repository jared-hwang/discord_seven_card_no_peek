import os, time
import discord
from discord.ext import commands
from seven_card_stud import *

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


peekgame = SevenCardNoPeek()
@bot.command(name='seatme')
async def seat_player(ctx):
    result = peekgame.seat_player(ctx.author.name)
    if result[0]:
        await ctx.send(f"Seated! Players: {', '.join(peekgame.players)}") 
    else:
        await ctx.send(f"{result[1]}. Players: {', '.join(peekgame.players)}") 

@bot.command(name='unseatme')
async def unseat_player(ctx):
    result = peekgame.unseat_player(ctx.author.name)
    if result[0]:
        await ctx.send(f"Unseated! Players: {', '.join(peekgame.players)}") 
    else:
        await ctx.send(f"{result[1]} Players: {', '.join(peekgame.players)}") 

@bot.command(name='unseat')
async def unseat_player(ctx, arg):
    result = peekgame.unseat_player(arg)
    if result[0]:
        await ctx.send(f"Unseated! Players: {', '.join(peekgame.players)}") 
    else:
        await ctx.send(f"{result[1]} Players: {', '.join(peekgame.players)}") 

@bot.command(name='newgame')
async def new_game(ctx):
    if len(peekgame.players) == 0:
        await ctx.send("No players!")
    peekgame.initialize_game()
    peekgame.next_round()
    for player in peekgame.players:
        await ctx.send(f":arrow_down: {player} :arrow_down: ")
        await ctx.send(f"{peekgame.player_dict[player].hand_string(peekgame.roundnum)}")

@bot.command(name='nextround')
async def next_round(ctx):
    peekgame.next_round()
    for player in peekgame.players:
        await ctx.send(f":arrow_down: {player} :arrow_down: ")
        await ctx.send(f"{peekgame.player_dict[player].hand_string(peekgame.roundnum)}")
    if peekgame.roundnum == 7:
        await ctx.send(peekgame.end_game())

@bot.command(name='reset_game')
async def reset_game(ctx):
    peekgame.reset_game()
    await ctx.send("Game reset.")

@bot.command(name='players')
async def players(ctx):
    await ctx.send(f"Players: {', '.join(peekgame.players)}")

bot.run(TOKEN)
