import discord
import random
from include import functions
from discord.ext import commands


class calculator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calculate(self, ctx):
        answer = functions.addNumbers(2, 1)
        print(answer)

    @commands.command()
    async def beg(self, ctx):
        person_list= ['Elon Musk: ', 'Jeff Bezoz: ', "Rahul 'Pappu' Gandhi: ", 'Donald Duck: ', "Sharu Khan: ", "Geeta Kumari Phogat: ", "Salmon Bhoi: ", "Bindi Man: ","Pawri Girl: ", "Kim Jong Un: ", "Prank Memer: ", "Justin Beiber: ", "Your Boy Baadshah: ","Your Drunk Self: ","Your Step Sister: ", "Ameer Khan: ", "That One Kid Who Always Keeps Running In The Restaraunt And Eventually Falls And Starts Crying: ","Bajrangi Bhai: ","Baman: ", "Poketwo: ", "TACO Shack: ", "Sehwag: "]
        type = random.randint(1, 2)
        person = random.choice(person_list)
        if type == 2:
            coins = random.randrange(100, 3000)
            await ctx.send(person + 'Gave ye ' + str(coins) + ' coins')
        else:
            response_list= ["be gone thot", "all right thot be gone now", "i share money & food with noone", "go ask somewhere else", "i share money with pawri members only", "oh hell nah", "the atm is out of order, sorry", "Ewwwww!!!! GET AWAY", "Can you not ???", "Nah, would rather not feed your gambling addiction", "No coins 4 u", "You get NOTHING", "Ther.is.no.coins.fo'.ye", "get lost u simp", "Back in my day we worked for a living", "You're too stanky", "paisa.com has stopped working", "Mission Failed Successfully"]
            rejection = random.choice(response_list)
            await ctx.send(person + ' ' + rejection)
        

def setup(client):
    client.add_cog(calculator(client))
