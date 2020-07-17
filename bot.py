import discord
from discord.ext import commands, tasks
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
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
	


client = commands.Bot(command_prefix = '.')

def getDate():
	storedDate = []
	for container in containers:
		
		storedDate.append(container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip())

	return storedDate

@client.event
async def on_ready():
	print('Bot is ready')


@task.loop(seconds = 60)
async def on_ready():	
	container = containers[0]
	title = container.find('h5',{"class" : "heading-05 NewsCard-module--title--1MoLu"}).text.strip()
	description = container.find('p',{"class" : "copy-02 NewsCard-module--description--3sFiD"}).text.strip()
	date = container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
	link = container.find('a', {"href" : True})

	if len(title) > 0:
		
		print(title)
		print(f'	{date}')
		print(f'	{description}\n')	
		if 'href' in link.attrs:		
			print(f"https://playvalorant.com{str(link.attrs['href'])} \n")

	getDate()




client.run('NzMzMTg4MjUzNTIzNjQwMzMx.Xw_ogg.mhTZ5JPsjfP16ds48f-CTqfYt-M')
