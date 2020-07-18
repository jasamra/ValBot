import discord
from discord.ext import commands, tasks
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
my_url = 'https://playvalorant.com/en-us/news/'
#opening connection/grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


#html parsing
page_soup = soup(page_html, "html.parser")
#grabs
containers = page_soup.findAll("div",{"class":"NewsArchive-module--newsCardWrapper--2OQiG"})

links = page_soup.findAll('a',{"href" : True})
	


client = commands.Bot(command_prefix = '!')

def getDate():
	storedDate = []
	for container in containers:
		
		storedDate.append(container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip())

	return storedDate

@client.event
async def on_ready():
	print('Bot')

@client.event
async def on_message(message):
	
		
		#await message.channel.send('yes')

	container = containers[0]
	title = container.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
	description = container.find('p',{"class" : "copy-02 NewsCard-module--description--3sFiD"}).text.strip()
	date = container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
	link = container.find('a', {"href" : True})



	if message.content =='!news':
		if len(title) > 0:
			await message.channel.send(title)
			#print(title)
			await message.channel.send(date)
			#print(f'	{date}')
			await message.channel.send(description)
			#print(f'	{description}\n')	
			if 'href' in link.attrs:

				await message.channel.send(f"https://playvalorant.com{str(link.attrs['href'])}")		
				#print(f"https://playvalorant.com{str(link.attrs['href'])} \n")

	if message.content == '!patch':

		patchTitles = []
		descriptionP = []
		datesP = []
		linksP = []
	
		for contain in containers:
			patch = contain.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
		#	print (patch)
			desP = contain.find('p',{"class" : "copy-02 NewsCard-module--description--3sFiD"}).text.strip()
			dateP = contain.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
			linkP = contain.find('a', {"href" : True})

			if patch.startswith('VALORANT Patch Notes'):
				patchTitles.append(patch)
				descriptionP.append(desP)
				datesP.append(dateP)
				linksP.append(linkP)

		#print(patchTitles[0])
		await message.channel.send(patchTitles[0])
		#print(f'	{datesP[0]}')
		await message.channel.send(datesP[0])
		#print(f'	{[descriptionP[0]]}\n')	
		await message.channel.send(descriptionP[0])
		if 'href' in linksP[0].attrs:
			await message.channel.send(f"https://playvalorant.com{str(linksP[0].attrs['href'])}")		
			#print(f"https://playvalorant.com{str(linksP[0].attrs['href'])} \n")
	
	

@client.command()
async def quit(ctx):
    sys.exit()
#@client.command()
#async def hello(ctx, arg):
#	await ctx.send(arg)

#@tasks.loop(seconds = 10)
#async def runtime_background_task():
	#new = True
	#while true:
		#print('Bot is ready')
	

		#getDate()




client.run('NzMzMTg4MjUzNTIzNjQwMzMx.XxFVVg.w1TqagJXOVi7avdJJEkFtuVVQwY')
