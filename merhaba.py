import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 1):
    await ctx.send("ne hehliyon ##### " * count_heh)

@bot.command()
async def topla(ctx,sayı=0,sayı2=0):
    x=sayı+sayı2
    await ctx.send(f"verdiğiniz sayıların toplamı {x} tir")

bot.run("IMPORTTOKEN")
