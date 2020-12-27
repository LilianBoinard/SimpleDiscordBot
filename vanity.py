import discord
from discord.ext import commands

channelBOT = 792058223447244800

def isChannelBOT(ctx):
    return ctx.message.channel.id == channelBOT

class CogVanity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.check(isChannelBOT)
    async def work(self, ctx):
        """ Vérifier qu'Hissiane est allumé """
        client = ctx.author
        contextAuthor = str(client)
        await ctx.send("I'm working " + contextAuthor + " Senpai ❤")
    
    @commands.command()
    @commands.check(isChannelBOT)
    async def hissiane(self, ctx):
        """ Embed d'Hissiane """
        embed = discord.Embed(title = "**Hissiane**", description = "created with ❤", colour=8860319)
        embed.set_author(name="Pyro#0239", icon_url="https://cdn.discordapp.com/avatars/494220268076662795/d5153c4674e12f146b8d835b72705f6f.png?size=128")
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/791333321106915378/90d3070545954f8e866c3808e065a063.webp?size=128", text = "2020")
        await ctx.send(embed = embed)
