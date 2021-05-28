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
DEEZER_PLAYLIST_URL = os.getenv('DEEZER_PLAYLIST_URL')

bot = commands.Bot(command_prefix='>')


@bot.command(name='hey')
async def greet(ctx):
    message = f'Hello, {ctx.author}, you sexy beast'
    await ctx.send(message)


@bot.command(name='sh')
async def share(ctx, args):
    try:
        conf_message = f'Attempting to share: {args}'
        print(conf_message)
        if spotify_integration.is_spotify_link(args):
            spotify_integration.add_to_spotify_playlist(args, SPOTIFY_PLAYLIST_URL)

            search_term = spotify_integration.get_song_search_term(args)
            deezer_url = deezer_integration.add_to_deezer_playlist(DEEZER_TOKEN, search_term, DEEZER_PLAYLIST_URL)
            await ctx.send(f'Added {deezer_url} and the above Spotify link for \'{search_term}\'')
        else:
            spotify_url = spotify_integration.search_for_track_url(args)
            spotify_integration.add_to_spotify_playlist(spotify_url, SPOTIFY_PLAYLIST_URL)

            deezer_url = deezer_integration.add_to_deezer_playlist(DEEZER_TOKEN, args, DEEZER_PLAYLIST_URL)
            await ctx.send(f'Added {spotify_url} and {deezer_url}')
    except Exception as e:
        await ctx.send(str(e))


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(f'{bot.user} is connected to the following guilds:')
        print(f' - {guild.name}:{guild.id}')


bot.run(DISCORD_TOKEN)
