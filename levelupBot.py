import discord
import os
import array
import time
from discord.ext import commands
import random

token = 'NjkxMzIxNTExNDA2OTkzNDg5.XniIiw.H97ENahDzOhoR-t2nLawG_3gDbA'

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')
    channel = bot.get_channel(692048756127957012)
    await channel.send(channel=channel, content='Hello')
    
@bot.command(name='levelup')
async def levelup1(ctx):
    await ctx.send('module sucessfully completed')

@bot.command(pass_context=True, name='create-role')
async def addrole(ctx):
    roleVer = 'test'
    user = ctx.message.author
    role = roleVer
    await ctx.send("""Attempting to Verify {}""".format(user))
    try:
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))
    except Exception as e:
        await ctx.send('There was an error running this command ' + str(e))
    else:
        await ctx.send("""Verified: {}""".format(user))
        
@bot.command(name='create-channel')
@commands.has_role('Role Manager')
async def create_channel(ctx, channel_name="morgz"):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await ctx.send(f'Creating new channel, name.parameter is {channel_name}')
        await ctx.send(f'Module completed. Thank You')
        await guild.create_text_channel(channel_name)

@bot.command(name='deactivate-levelupbot')
@commands.has_role('Bot Developer')
async def create_channel(ctx, channel_name="morgz"):
    await ctx.send("Goodbye")
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You don't have the privileges to invoke this command")

bot.run(token) & client.run(token)
