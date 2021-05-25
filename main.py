# main.py
import os
from dotenv import load_dotenv
from discord.ext import commands
import spotify_integration
import deezer_integration

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DEEZER_TOKEN = os.getenv('DEEZER_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')
SPOTIFY_PLAYLIST_URL = os.getenv('SPOTIFY_PLAYLIST_URL')

bot = commands.Bot(command_prefix='>')


@bot.command(name='hey')
async def greet(ctx):
    message = f'Hello, {ctx.author}, you sexy beast'
    await ctx.send(message)


@bot.command(name='sh')
async def share(ctx, args):
    conf_message = f'Attempting to share: {args}'
    print(conf_message)
    if spotify_integration.is_spotify_link(args):
        spotify_integration.add_to_spotify_playlist(args, SPOTIFY_PLAYLIST_URL)
    else:
        await ctx.send('Sorry, that\'s not a valid Spotify link.')


@bot.command(name='dsh')
async def deezer_share(ctx, args):
    conf_message = f'Attempting to share on deezer: {args}'
    print(conf_message)
    deezer_integration.add_to_deezer_playlist(DEEZER_TOKEN, args)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(f'{bot.user} is connected to the following guilds:')
        print(f' - {guild.name}:{guild.id}')


bot.run(DISCORD_TOKEN)
