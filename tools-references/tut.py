import discord
import typing
import json
from discord.ext import commands

file = open("config.json", "r")
config = json.load(file)
prefix = config["Prefix"]
token = config["Token"]

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guild.member_count)) + ' users'))
    print("Bot is ready")


bad_words = ["gf", "simp", "pokimane"]


@client.event
async def on_message(msg):
    for word in bad_words:
        if word in msg.content:
            await msg.delete()
    await client.process_commands(msg)


@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, CommandNotFound):
        pass


@client.command()
async def hello(ctx, mem: discord.Member):
    embed = discord.Embed(
        title=mem.name, description=mem.mention, color=0x42a7f5)
    embed.set_thumbnail(url=mem.avatar_url)
    embed.set_image(url=mem.avatar_url)
    embed.add_field(name="ID", value=mem.id, inline=True)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def gg(ctx, *, x: typing.Optional[str]):
    if x:
        await ctx.send(x)


fl = open("rules.txt", "r")
lst = fl.readlines()


@client.command(aliases=['rules'])
async def rule(ctx, *, num):
    await ctx.send(lst[int(num) - 1])


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, mem: discord.Member, *, reason='No reason given'):
    try:
        await mem.send('You are kicked for ' + reason)
    except:
        await ctx.send('Cannot send message in dm but, ' + mem.name + ' has been kicked')
    await mem.kick(reason=reason)
    await ctx.send(mem.name + ' has been kicked')


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, mem: discord.Member, *, reason='No reason given'):
    try:
        await mem.send('You are banned for ' + reason)
    except:
        await ctx.send('Cannot send message in dm but, ' + mem.name + ' has been kicked')
    await mem.ban(reason=reason)
    await ctx.send(mem.name + ' has been banned')


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, member, *, reason):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + ' has been unbanned because ' + reason)
            return


@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason):
    muted_role = ctx.guild.get_role(708608491706777600)
    await member.add_roles(muted_role)
    await ctx.send(member.mention + ' has been muted for ' + reason)


@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member, *, reason):
    muted_role = ctx.guild.get_role(708608491706777600)
    await member.remove_roles(muted_role)
    await ctx.send(member.mention + ' has been unmuted for ' + reason)

client.run(token)
