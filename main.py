import scrape
import sys
import random
import pyperclip
# import webbrowser

try: query = sys.argv[1]
except IndexError: query = 0

gallery_list = scrape.download_list(query)
gif_url = random.choice(gallery_list)
url = 'https://i.imgur.com/' + gif_url[gif_url.find('/', 2) + 1:] + '.gif'

# webbrowser.open_new_tab(url)
pyperclip.copy(url)

print("GIF (%s) copied to clipboard!" % (url))