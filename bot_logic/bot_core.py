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
protected_roles = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hello():
    await bot.say('Hello!')

@bot.command()
async def list_roles(member : discord.Member):
    role_list = []
    for r in member.roles:
        role_list.append(r.name)
    await bot.say(', '.join(role_list))

@bot.command(pass_context=True)
async def join(ctx, role : discord.Role):
    if role not in protected_roles:
        bot.add_roles(ctx.message.author, role)
        await bot.say(' '.join(['Member:', ctx.message.author.name, 'joined', role.name]))
    else:
        await bot.say('This role is protected. Please join via discord.')

@bot.command()
async def protect_roles(*roles : discord.Role):
    if not isinstance(roles, collections.Iterable):
        ra = [].append(roles)
    else:
        ra = roles
    protected_roles.extend(ra)
    await bot.say('These roles are currently protected: ' + ', '.join(protected_roles))

@bot.command()
async def release_roles(*roles : discord.Role):
    if not isinstance(roles, collections.Iterable):
        ra = [].append(roles)
    else:
        ra = roles
    protected_roles = [x for x in protected_roles if x not in ra]
    await bot.say('These roles are currently protected: ' + ', '.join(protected_roles))
    
    
with open('token.txt') as f:
    bot.run(f.readline())