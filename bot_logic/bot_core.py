"""
Code Discord bot module.
"""

import discord
import collections

from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.event
async def on_message(message : discord.Message):
    if bot.user in message.mentions:
        await message.channel.send(message.author.mention)
        
    await bot.process_commands(message)


@bot.command
async def hello(ctx):
    await ctx.send('Hello!')


#bot.run("Token here")
with open('token.txt') as f:
    bot.run(f.readline())
