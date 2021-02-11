from bot_token import token
import discord
from discord.ext import commands
import datetime
import random

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

bot.remove_command('help')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def add(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Entra nel server minecraft: battlemine.sparked.network"))
    print("Il bot e' pronto")

@bot.command()
async def ip(ctx):
        embed = discord.Embed(title="IP", description="battlemine.sparked.network", color=0x00ff00)
        embed.add_field(name="RolePlay", value="1.12.2", inline=False)
        embed.add_field(name="BedWars", value="1.8.x - 1.12.2", inline=False)
        embed.add_field(name="Prison", value="1.8.x - 1.12.2", inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def stato(ctx):
        embed = discord.Embed(title="Stato Server", description="", color=0xffd600)
        embed.add_field(name="Generale", value="In Manutenzione", inline=False)
        embed.add_field(name="RolePlay", value="Beta", inline=False)
        embed.add_field(name="BedWars", value="Beta", inline=False)
        embed.add_field(name="Prison", value="In Manutenzione", inline=False)
        await ctx.send(embed=embed)
    
@bot.command()
async def sium(ctx):
        await ctx.message.delete()
        await ctx.send("https://tenor.com/view/ronaldo-sium-ronaldo-siuuu-sium-ronaldo-gif-19193460")

@bot.command()
async def tiaspecto(ctx):
        await ctx.message.delete()
        await ctx.send("https://tenor.com/view/siccer-calcio-cristiano-football-ronaldo-gif-19923672")

@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Ecco I Miei Comandi", description="", color=0x00ff00)
        embed.add_field(name=">helpmeme", value="Meme e gif", inline=False)
        embed.add_field(name=">helpinfo", value="Informazioni", inline=False)
        await ctx.send(embed=embed)
    
@bot.command()
async def helpmeme(ctx):
        embed = discord.Embed(title="Ecco I Miei Comandi Meme", description="", color=0x00ffff)
        embed.add_field(name=">sium", value="SIUUUUUUUUUUMMMMMM", inline=False)
        embed.add_field(name=">tiaspecto", value="SCEGLI E-CAMPUS! TI ASPEKTO", inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def helpinfo(ctx):
        embed = discord.Embed(title="Ecco I Miei Comandi Info", description="", color=0x00FFFF)
        embed.add_field(name=">stato", value="Mostra lo stato dei server", inline=False)
        embed.add_field(name=">ip", value="Mostra l'ip del server", inline=False)
        await ctx.send(embed=embed)

@bot.command()
@commands.has_role('Staff')
async def clear(ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send("Ho cancellato i messaggi!")

@bot.command()
@commands.has_role("StaffX")
async def ban(ctx, member : discord.Member, reason=None):
    """Bans a user"""
    if reason == None:
        await ctx.send(f"Hey {ctx.author.mention}, Devi scrivere un motivo!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)

@bot.command()
@commands.has_role("StaffX")
async def pardon(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.banned_users

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)

@bot.command()
async def freekey(ctx):
    responses = ["https://tenor.com/view/coconut-malled-gif-20280826",
                 "https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825",
                 "https://tenor.com/view/stick-bugged-stick-bugged-get-stick-bugged-lol-gif-18039349",
                 "https://tenor.com/view/caught-yo-ass-in4k-gif-20281079",]
    await ctx.send(f"{random.choice(responses)}")

@bot.command
async def on_member_join(ctx, *, member):
    channel = member.server.get_channel("channel id")
    fmt = 'Benvenuto {1.name} a BattleMine, {0.mention}'
    await ctx.send(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(ctx, *, member):
    channel = member.server.get_channel("channel id")
    fmt = '{0.mention} è uscito/è stato kickato dal server.'
    await ctx.send_message(channel, fmt.format(member, member.server))

bot.run(token)