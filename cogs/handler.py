import discord
from discord.ext import commands, tasks


class handler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @tasks.loop(minutes = 30)
    async def change_stat(self):
        await self.client.change_presence(status= discord.Status.idle, activity= discord.Activity(type= discord.ActivityType.watching, name=str(len(self.client.users)) + ' users'))

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_stat.start()
        print('Bot is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' Pong : {round(self.client.latency * 1000)} ms')


def setup(client):
    client.add_cog(handler(client))
