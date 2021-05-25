# main.py
import os
from dotenv import load_dotenv
from discord.ext import commands
import spotify_integration

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
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
