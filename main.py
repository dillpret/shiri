# main.py
import os
from dotenv import load_dotenv
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX')
SPOTIFY_PLAYLIST_URL = os.getenv('SPOTIFY_PLAYLIST_URL')

SPOTIFY_ACCESS_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"

scope = "playlist-modify-public"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


bot = commands.Bot(command_prefix='>')


def add_to_spotify_playlist(track_link):
    sp.playlist_add_items(SPOTIFY_PLAYLIST_URL, [track_link])


def is_spotify_link(string):
    print(string)
    regex = r'^(spotify:|https://[a-z]+\.spotify\.com/)'
    if re.search(regex, string):
        return True
    else:
        return False


@bot.command(name='hey')
async def greet(ctx):
    message = f'Hello, {ctx.author}, you sexy beast'
    await ctx.send(message)


@bot.command(name='sh')
async def share(ctx, args):
    conf_message = f'Attempting to share: {args}'
    print(conf_message)
    if is_spotify_link(args):
        add_to_spotify_playlist(args)
    else:
        await ctx.send('Sorry, that\'s not a valid Spotify link.')

    # search_results = sp.search(args, type='track')
    # print(search_results)


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
