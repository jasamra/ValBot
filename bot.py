import discord
from discord.ext import commands, tasks
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



URL = 'https://playvalorant.com/en-us/news/'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready')


@task.loop(seconds = 60)
async def function():
	pass


client.run('NzMzMTg4MjUzNTIzNjQwMzMx.Xw_ogg.mhTZ5JPsjfP16ds48f-CTqfYt-M')
