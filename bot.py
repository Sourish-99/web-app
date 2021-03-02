import os
import json
import discord
from discord.ext import commands

with open("config.json", "r") as file:
    config = json.load(file)
    prefix = config["Prefix"]
    token = config["Token"]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, commands.CommandNotFound):
        return
    if isinstance(exc, commands.NotOwner):
        return await ctx.send('Only bot owner has permission to this command')
    raise exc


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} has been loaded')
    except:
        await ctx.send(f'{extension} is already loaded or not found')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} has been unloaded')
    except:
        await ctx.send(f'{extension} is already unloaded or not found')


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.reload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} has been reloaded')
    except:
        await ctx.send(f'There is an error while reloading {extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]} loaded')

client.run(token)
