from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import aiohttp
import asyncio

search = 'How to unlock Hifumi Togo in Persona 5 Royal'
url = 'https://www.google.com/search'
access_key = "1f38bdc246e64a7a9e7545004c7cf282"
second_access_key = "a9d349126d4cbc16e0d4e91b07c3f87d"
#https://apiflash.com/dashboard/get_started
api = "https://api.apiflash.com/v1/urltoimage?access_key="+access_key+"&wait_until=page_loaded&response_type=json&extract_text=true&element=body&url="

#https://screenshotlayer.com/dashboard
second_api = "https://api.screenshotlayer.com/api/capture?access_key="+second_access_key+"&viewport=1920x1080&fullpage=1&url="




#print(first_link['href'])

async def screenshot(searchprompt):
	global api
	global search
	search = searchprompt
	headers = {
	'Accept' : '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
	parameters = {'q': search}

	#print(api)
	content = requests.get("https://www.google.com/search", headers = headers, params = parameters).text
	soup = BeautifulSoup(content, 'html.parser')

	search = soup.find(id = 'search')
	first_link = search.find('a')
	#print(first_link['href'])
	webshot = requests.get(api + first_link['href'])
	print(webshot.json())
	return webshot.json()["url"]


#screenshot("How to unlock judgement confident in persona 5")