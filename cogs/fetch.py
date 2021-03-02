import typing
import httpx
import discord
from io import BytesIO
from discord.ext import commands, tasks


class fetch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, *, loca: typing.Optional[str]):
        if not loca: return await ctx.send('city name not provided')

        try:
            async with httpx.AsyncClient() as client:
                req = await client.get('https://api.weatherapi.com/v1/current.json?key=e7ef135cd7b848b0ace64727210402&q=' + loca)
        except:
            return await ctx.send('Could not connect to socket')

        if req.status_code == 200:
            data = req.json()
        elif req.status_code == 401:
            return await ctx.send('Api key is invalid')
        else:
            return await ctx.send('unknown error occured')

        embed = discord.Embed(title='Weather', description= '```' + data["location"]["name"] + ' - ' + data["current"]["condition"]["text"] + '```', color=0x42a7f5)
        embed.set_thumbnail(url= 'https:' + data["current"]["condition"]["icon"])
        embed.add_field(name="Region", value= data["location"]["region"], inline=True)
        embed.add_field(name="Country", value= data["location"]["country"], inline=True)
        embed.add_field(name="Continent", value= data["location"]["tz_id"].split("/")[0], inline=True)
        embed.add_field(name="Date", value= data["location"]["localtime"].split()[0], inline=True)
        embed.add_field(name="Time", value= data["location"]["localtime"].split()[1], inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def wasted(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        try:
            async with httpx.AsyncClient() as client:
                req = await client.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}")
        except:
            return await ctx.send('Could not connect to api')

        img = await req.aread()
        file = discord.File(fp=BytesIO(img), filename="wasted.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://wasted.png")
        await ctx.send(embed=embed, file=file)

    @commands.command()
    async def trigger(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        try:
            async with httpx.AsyncClient() as client:
                req = await client.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}")
        except:
            return await ctx.send('Could not connect to api')

        img = await req.aread()
        file = discord.File(fp=BytesIO(img), filename="triggered.gif")
        embed = discord.Embed()
        embed.set_image(url="attachment://triggered.gif")
        await ctx.send(embed=embed, file=file)


def setup(client):
    client.add_cog(fetch(client))