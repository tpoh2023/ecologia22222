import discord
from discord.ext import commands
import os
import random

list_advice = ["сортируйте мусор", "занимайтесь посадкой деревьев", "переходите на электромобили"]
list_website = ["https://ru.wikipedia.org/wiki/Глобальное_потепление", "https://trends.rbc.ru/trends/green/641402fe9a7947520b87e078", "https://www.kp.ru/family/ecology/globalnoe-poteplenie/"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    image = random.choice(os.listdir('images'))
    with open(f'images/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command()
async def info(ctx):
    website = random.choice(list_website)
    await ctx.send(website)

@bot.command()
async def advice(ctx):
    advice = random.choice(list_advice)
    await ctx.send(advice)

bot.run("MTIyNTgzNzI1ODU5NTIzODAxMA.GZN6xo.CJY910JY54FrR75BKGq2aS8RPAABcxostFWMfQ")