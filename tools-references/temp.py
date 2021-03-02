@commands.command(usage="<Stadt>")
   async def weather(self, ctx, *, city):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://api.openweathermap.org/data/2.5/weather?zip={city}&appid=KEY") as r:
                data = await r.json()
                icon = data['weather'][0]['icon']
                cleared_data = {
                    'Location:': data['name'],
                    'Weather:': f"{data['weather'][0]['main']} - {data['weather'][0]['description']}",
                    'Weather icon:': f"https://openweathermap.org/img/wn/{icon}@2x.png",
                    'Temperature:': f"{int((float(data['main']['temp'])))}°C/{int((float(data['main']['temp']) * 1.8) + 32)}°F",
                    'Feels like:': f"{int((float(data['main']['feels_like'])))}°C/{int((float(data['main']['feels_like']) * 1.8) + 32)}°F",
                    'Humidity:': f"{int((float(data['main']['humidity'])))}%",

                    'Sunrise:': datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                    'Sunset:': datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),

                }
                embed = discord.Embed(title=f"Weather now", color=0xdb1b1b)
                for key, value in cleared_data.items():
                    embed.add_field(name=key, value=value, inline=True)
                    embed.set_thumbnail(url=f"https://openweathermap.org/img/wn/{icon}@2x.png")
                await ctx.send(embed=embed)


@commands.command()
   async def wasted(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        wastedsession = aiohttp.ClientSession()
        wastedget = await wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}") as img:
            if status != 200:
                await ctx.send("Unable to get image")
                await wastedsession.close()

            else:
                data = io.BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'wasted.jpg'))
                await wastedsession.close()

@commands.command(name='comment')
async def comment(self, ctx, *, content):
    pfp = ctx.author.avatar_url_as(format='png')
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://some-random-api.ml/canvas/youtube-comment?avatar={pfp}&username={ctx.author.display_name}&comment={content}') as r:
            if r.status == 200:
                await ctx.send(f"https://some-random-api.ml/canvas/youtube-comment?avatar={pfp}&username={ctx.author.display_name}&comment={content}/")
            else:
                await ctx.send("An Error has occrred~")
