import requests
import random
from bs4 import BeautifulSoup

def download_list(query):
	url = "https://imgur.com/"
	sort = {'query': ['score', 'relevance', 'time'], 'no_query': ['hot/time', 'top', 'hot/viral']}
	if (query):
		url += 'search/' + random.choice(sort['query']) + '/all?q_type=anigif&q_all=' + query
	else:
		url += random.choice(sort['no_query'])

	html = requests.get(url).content
	soup = BeautifulSoup(html, 'html.parser')

	gallery_list = []
	for link in soup.find_all('a'):
		if 'gallery' in link.get('href'):
			gallery_list.append(link.get('href'))
	return gallery_list
