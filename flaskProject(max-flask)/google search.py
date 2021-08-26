


import requests

# get the API KEY here: https://developers.google.com/custom-search/v1/overview
key = 'AIzaSyDWD4dfCQ1oHe8p6bNPS5wdH1PTq00h63U'
API_KEY = key
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "<INSERT_YOUR_SEARCH_ENGINE_ID_HERE>"

# the search query you want
query = "python"
# using the first page
page = 1
# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"