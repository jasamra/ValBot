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
	
#for container in containers:

def storedDates():
	storedDate = []
	for container in containers:
		dates = container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
		storedDate.append(dates)


	return storedDate

def PrevDates():
	container = containers[0]
	datePrev = container.find('p',{"class" : "NewsCard-module--published--37jmR"}).text.strip()
	return datePrev

def patch():
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


	
	#if len(patchTitles[0]) > 0:
		
	print(patchTitles[0])
	print(f'	{datesP[0]}')
	print(f'	{[descriptionP[0]]}\n')	
	if 'href' in linksP[0].attrs:		
		print(f"https://playvalorant.com{str(linksP[0].attrs['href'])} \n")
	

def scrape():
	

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
	



#scrape()
#patch()
