import discord
from discord.ext import commands


channelBOT = 792058223447244800

def isChannelBOT(ctx):
    return ctx.message.channel.id == channelBOT

class CogAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.check(isChannelBOT)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
        """ Kicker un utilisateur """
        await ctx.guild.kick(user, reason = reason)
        embed = discord.Embed(title = "**Kick**", description = "Un membre a été kick.", color=8860319)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = user.avatar_url)
        embed.add_field(name = "Membre kick", value = user.name, inline = True)
        embed.add_field(name = "Raison", value = reason, inline = True)
        embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/791333321106915378/90d3070545954f8e866c3808e065a063.webp?size=128", text = "Hissiane")

        await ctx.send(embed = embed)
        
    @commands.command()
    @commands.check(isChannelBOT)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
        """ Bannir un utilisateur """
        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(title = "**Banissement**", description = "Un membre a été banni.", color=8860319)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = user.avatar_url)
        embed.add_field(name = "Membre banni", value = user.name, inline = True)
        embed.add_field(name = "Raison", value = reason, inline = True)
        embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/791333321106915378/90d3070545954f8e866c3808e065a063.webp?size=128", text = "Hissiane")

        await ctx.send(embed = embed)
        
    @commands.command()
    @commands.check(isChannelBOT)
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        """ Débannir un utilisateur """
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        
        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
        
                embed = discord.Embed(title = "**Débanissement**", description = "Un membre a été débanni.", color=8860319)
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                embed.set_thumbnail(url = user.avatar_url)
                embed.add_field(name = "Membre débanni", value = user.name, inline = True)
                embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
                embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/791333321106915378/90d3070545954f8e866c3808e065a063.webp?size=128", text = "Hissiane")

                await ctx.send(embed = embed)
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx):
        """ Nettoyer un salon de ses messages """
        messages = await ctx.channel.history().flatten()
        await ctx.send("Nettoyage des messages...")
        for message in messages:
            await message.delete()
        await ctx.send("Effectué !")
