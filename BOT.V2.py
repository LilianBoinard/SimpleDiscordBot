import discord
from discord.ext import commands
import asyncio
import vanity
import admin
import music
import hissiane

from colorama import init, Fore

botToken = ""

def logo():
    print(Fore.MAGENTA + "\n")
    print("████████▄  ▀█████████▄     ▄█    █▄   ")
    print("███   ▀███   ███    ███   ███    ███  ")
    print("███    ███   ███    ███   ███    ███  ")
    print("███    ███  ▄███▄▄▄██▀   ▄███▄▄▄▄███▄▄")
    print("███    ███ ▀▀███▀▀▀██▄  ▀▀███▀▀▀▀███▀ ")
    print("███    ███   ███    ██▄   ███    ███  ")
    print("███   ▄███   ███    ███   ███    ███  ")
    print("████████▀  ▄█████████▀    ███    █▀   ")
    print('discord.py v.{0}'.format(discord.__version__))
    print(Fore.WHITE + "\n")
    print("--------------------------------------")
logo()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description="Hey, je suis Hissiane", intents=intents)

masterID = 494220268076662795

channelBOT = 792058223447244800
channelERRORS = 792071586861416498
channelANNONCES = 792058610526978109


def isMaster(ctx):
    return ctx.message.author.id == masterID

def isChannelBOT(ctx):
    return ctx.message.channel.id == channelBOT



#----------Events-----------#
@bot.event
async def on_ready():
    print("Pret !")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Hissiane'))
    await bot.get_channel(channelBOT).send("I am starting ❤")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un/des argument(s).")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Baka, cette commande n'existe pas.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("Tu dois être mon maitre pour utiliser cette commande.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Tu ne peux pas utiliser cette commande, tu n'as peut-être pas les droits ou ne l'utilise pas au bon endroit.")    
    elif isinstance(error, commands.MessageNotFound):
        await ctx.send("Désolé, le message n'a pas été trouvé.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Désolé, le membre n'a pas été trouvé.")
    elif isinstance(error, commands.UserNotFound):
        await ctx.send("Désolé, l'utilisateur n'a pas été trouvé.")
    elif isinstance(error, commands.ChannelNotFound):
        await ctx.send("Désolé, le membre n'a pas été trouvé.")
    elif isinstance(error, commands.ChannelNotReadable):
        await ctx.send("Je n'ai pas la permission de lire des messages dans ce canal.")
    elif isinstance(error, commands.RoleNotFound):
        await ctx.send("Désolé, je n'ai pas trouvé ce role.")
    else:
        await bot.get_channel(channelERRORS).send(error)
    
@bot.event
async def on_member_join(member):
    embed = discord.Embed(title = "**Arrivage**", description = "Un membre nous a rejoint.", color=8860319)
    embed.set_author(name = member.name, icon_url = member.avatar_url)
    embed.set_thumbnail(url = member.avatar_url)
    embed.add_field(name = "Membre en question:", value = member.name, inline = True)
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/791333321106915378/90d3070545954f8e866c3808e065a063.webp?size=128", text = "Hissiane")
    
    await member.guild.get_channel(channelANNONCES).send(embed = embed)
    
@bot.event
async def on_member_remove(member):
    embed = discord.Embed(title = "**Départ**", description = "Un membre nous a quitté.", color=8860319)
    embed.set_author(name = member.name, icon_url = member.avatar_url)
    embed.set_thumbnail(url = member.avatar_url)
    embed.add_field(name = "Membre en question:", value = member.name, inline = True)
    embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/791333321106915378/90d3070545954f8e866c3808e065a063.webp?size=128", text = "Hissiane")
    
    await member.guild.get_channel(channelANNONCES).send(embed = embed)  
#----------Events-----------#
        
#----------Commands-----------#
bot.add_cog(admin.CogAdmin(bot))
bot.add_cog(music.CogMusic(bot))
bot.add_cog(vanity.CogVanity(bot))
#----------Commands-----------#  
bot.run(botToken)