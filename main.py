import sys
import scrape
import random
import webbrowser
import pyperclip

if len(sys.argv) > 1: query = sys.argv[1]
else: query = 0

gallery_list = scrape.download_list(query)
gif_url = random.choice(gallery_list)
url = 'https://i.imgur.com/' + gif_url[gif_url.find('/', 2) + 1:] + '.gif'
# webbrowser.open_new_tab(url)

pyperclip.copy(url)
print("gif link copied to clipboard!")