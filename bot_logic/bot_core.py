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
guildName = "pingable"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.event
async def on_message(message : discord.Message):
    if bot.user.mentioned_in(message):
        atList = [ m.mention for m in message.mentions if m.mention != bot.user.mention]
        if len(atList) > 0:
            if guildName in [r.name for r in message.author.roles]:
                await message.channel.send(" ".join(atList))
            else:
                await message.channel.send("You need the correct role to use this feature, please contact the bot administrator.")
        else:
            await message.channel.send(message.author.mention)
        
    await bot.process_commands(message)


@bot.command
async def hello(ctx):
    await ctx.send('Hello!')


#bot.run("Token here")
with open('token.txt') as f:
    bot.run(f.readline())
