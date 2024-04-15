import webbrowser


# # opening browser
# webbrowser.open("http://pypi.org")

# # serach on searchengine

def search_on_searchengine(query, searchengine):
    search_engines = {
        "google": "https://www.google.com/search?q={}",
        "yahoo": "http://search.yahoo.com/search?p={}",
        "bing": "https://www.bing.com/search?q={}"
    }

    if searchengine in search_engines:
        print("search engine found")
        search_url = search_engines[searchengine].format(query)
        webbrowser.open(search_url)
    else:
        raise IOError("Search engine not found")


search_on_searchengine("python", "google")
search_on_searchengine("python", "yahoo")
search_on_searchengine("python", "bing")
