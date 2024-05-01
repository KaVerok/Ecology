import random
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def info(ctx):
    await ctx.send('Привет. Я бот об экологии. Мы можем сообщать новости и т.д. ')

@bot.command()
async def problems(ctx,count=1):
    eco_problems=['Загрязнение воды', "Загрязнение воздуха","Вымирание животных","Природный катаклизм"]
    for i in range(count):
        await ctx.send(eco_problems[i])

@bot.command()
async def pictures(ctx):
    eco_pictures = os.listdir('eco')
    random_pictures=random.choice(eco_pictures)
    with open(f'eco/{random_pictures}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")