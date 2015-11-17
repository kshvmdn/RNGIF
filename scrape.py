import requests
import random
from bs4 import BeautifulSoup

def download_list(query):
	if (query):
		sort = ['score', 'relevance', 'time']
		url = 'https://imgur.com/search/' + random.choice(sort) + '/all?q_type=anigif&q_all='+query
	else:
		sort = ['hot/time', 'top', 'hot/viral']
		url = 'https://imgur.com/' + random.choice(sort)

	html = requests.get(url).content
	soup = BeautifulSoup(html, 'html.parser')

	gallery_list = []
	for link in soup.find_all('a'):
		if 'gallery' in link.get('href'):
			gallery_list.append(link.get('href'))
	return gallery_list
