# main.py
import os
from dotenv import load_dotenv
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')

SPOTIFY_ACCESS_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"
SPOTIFY_PLAYLIST_URL = "https://api.spotify.com/v1/playlists/4BvNLwSbqsrwtHXZ1erfAz/tracks"

# SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


bot = commands.Bot(command_prefix='>')


@bot.command(name='hey')
async def greet(ctx):
    message = f'Hello, {ctx.author}, you sexy beast'
    print(message)
    await ctx.send(message)


@bot.command(name='sh')
async def share(ctx, args):
    message = f'Received link: {args}'
    print(message)
    await ctx.send(message)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(f'{bot.user} is connected to the following guilds:')
        print(f' - {guild.name}:{guild.id}')


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     if message.content == 'some song':
#         await message.channel.send('Here I will send link')


bot.run(TOKEN)
