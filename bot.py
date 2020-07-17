import discord
from discord.ext import commands

URL = 'https://playvalorant.com/en-us/news/'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready')

def get_news():
		request = Request("https://playvalorant.com/en-us/news/", headers={'User-Agent': 'Mozilla/5.0'})


client.run('NzMzMTg4MjUzNTIzNjQwMzMx.Xw_ogg.mhTZ5JPsjfP16ds48f-CTqfYt-M')
