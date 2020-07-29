import discord
from discord.ext import commands, tasks
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
import asyncio



client = commands.Bot(command_prefix = '!')
my_url = 'https://playvalorant.com/en-us/news/'
		#opening connection/grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


#html parsing
page_soup = soup(page_html, "html.parser")
#grabs
containers = page_soup.findAll("div",{"class":"NewsArchive-module--newsCardWrapper--2OQiG"})
		
container = containers[0]




@client.event
async def on_ready():
	print('Bot')
	
	
#@tasks.loop(seconds = 1)
#	await client.wait_until_ready()
	#counter = 0
	#channel = client.get_channel(733192141756694602)
#	while not client.is_closed():
	#	counter += 1
	#	await channel.send(counter)
	#	await asyncio.sleep(10)
	

async def autoNews():
	#await client.wait_until_ready()
	channel = client.get_channel(733918383803727922)
	title = container.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
	prevTitle = title
	
	while not client.is_closed():

		my_url = 'https://playvalorant.com/en-us/news/'
		#opening connection/grabbing the page
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()


		#html parsing
		page_soup = soup(page_html, "html.parser")
		#grabs
		
		new = page_soup.findAll("div",{"class":"NewsArchive-module--newsCardWrapper--2OQiG"})
		newContainer = new[0]
	
		if prevTitle != newContainer.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip():
			
		#await channel.send('error1')
			title = newContainer.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
			description = newContainer.find('p',{"class" : "copy-02 NewsCard-module--description--3sFiD"}).text.strip()
			date = newContainer.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
			link = newContainer.find('a', {"href" : True})
			
			
			#await channel.send(title)
				#print(title)
			#await channel.send(date)
				#print(f'	{date}')
			#await channel.send(description)
				#print(f'	{description}\n')	
			if 'href' in link.attrs:

				if link.attrs['href'].startswith('https://www.youtube.com'):

					await message.channel.send(f"{title}\n{date}\n{description}\n{str(link.attrs['href'])}")
					
				#print(f"https://playvalorant.com{str(link.attrs['href'])} \n")
				else:

					await message.channel.send(f"{title}\n{date}\n{description}\nhttps://playvalorant.com{str(link.attrs['href'])}")

			prevTitle = title		


		await asyncio.sleep(120)

@client.event
async def on_message(message):
		
	#await message.channel.send('yes')

	if message.content =='!news':

		my_url = 'https://playvalorant.com/en-us/news/'
		#opening connection/grabbing the page
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()


		#html parsing
		page_soup = soup(page_html, "html.parser")
		#grabs
		containers = page_soup.findAll("div",{"class":"NewsArchive-module--newsCardWrapper--2OQiG"})
		
		container = containers[0]
		title = container.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
		description = container.find('p',{"class" : "copy-02 NewsCard-module--description--3sFiD"}).text.strip()
		date = container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
		link = container.find('a', {"href" : True})


		
		#await message.channel.send(f'{title}\n{date}\n{description}')
			#print(title)
		#await message.channel.send(date)
			#print(f'	{date}')
		#await message.channel.send(description)
			#print(f'	{description}\n')	
		if 'href' in link.attrs:

			if link.attrs['href'].startswith('https://www.youtube.com'):

				await message.channel.send(f"{title}\n{date}\n{description}\n{str(link.attrs['href'])}")
					
				#print(f"https://playvalorant.com{str(link.attrs['href'])} \n")
			else:

				await message.channel.send(f"{title}\n{date}\n{description}\nhttps://playvalorant.com{str(link.attrs['href'])}")

	if message.content == '!patch':
		my_url = 'https://playvalorant.com/en-us/news/'
		#opening connection/grabbing the page
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()


		#html parsing
		page_soup = soup(page_html, "html.parser")
		#grabs
		

		containers = page_soup.findAll("div",{"class":"NewsArchive-module--newsCardWrapper--2OQiG"})

		container = containers[0]
		title = container.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
		description = container.find('p',{"class" : "copy-02 NewsCard-module--description--3sFiD"}).text.strip()
		date = container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
		link = container.find('a', {"href" : True})


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
		#await message.channel.send(patchTitles[0])
		#print(f'	{datesP[0]}')
		#await message.channel.send(datesP[0])
		#print(f'	{[descriptionP[0]]}\n')	
		#await message.channel.send(descriptionP[0])
		if 'href' in linksP[0].attrs:
				await message.channel.send(f"{patchTitles[0]}\n{datesP[0]}\n{descriptionP[0]}\nhttps://playvalorant.com{str(linksP[0].attrs['href'])}")		
			#print(f"https://playvalorant.com{str(linksP[0].attrs['href'])} \n")

#@tasks.loop(seconds = 10)
#async def check_for_news():	

	

client.loop.create_task(autoNews())






client.run('')
