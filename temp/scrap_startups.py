from bs4 import BeautifulSoup as bs
import requests
import json
import urllib

# base_url = 'https://startupbase.com.br/startups?q=&states=S%C3%A3o%20Paulo&cities=all&groups=all&targets=all&phases=all&models=all&badges=all'
#
# pagina  = requests.get(base_url)
# soup = bs(pagina.content, "html.parser")
# section = soup.find("section", {"class": "search-body__results"})
# nomes = [ nm for nm in section.findAll("div", {"class": "organization__summary"})]
# import pdb; pdb.set_trace()
# print("FIM")
# import pdb; pdb.set_trace()
# print("FIM")
# --------------------------------------------------------------------------------------
# resposta ajax

# ------------------------------- USANDO SELENIUM --------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

#-------------------------------------------------------------------------------------
url_1 = 'https://api.mixpanel.com/decide/?'
head_1 = {
        "Origin": "https://startupbase.com.br",
        "Referer": "https://startupbase.com.br/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}
query_1 = {
        "verbose": "1",
        "version": "1",
        "lib": "web",
        "token": "8f58fb809eaf8fbc72a2c6c65c268456",
        "ip": "1",
        "_": "1559311776852"
}

pg = requests.get(url_1, headers = head_1, params = query_1)
new_response = '{"notifications":[],"config":{"enable_collect_everything":true}}'
pg.__dict__['_content'] = new_response
max_age = pg.headers['Access-Control-Max-Age']
import pdb; pdb.set_trace()


page = 0
page = str(page)
url = 'https://fwtbnxlfs6-dsn.algolia.net/1/indexes/*/queries?'
query_string = 'x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser%3B%20angular%20(7.2.15)%3B%20angular-instantsearch%20(3.0.0-beta.1)%3B%20angular-instantsearch-server%20(3.0.0-beta.1)%3B%20instantsearch.js%20(3.5.3)%3B%20JS%20Helper%20(2.28.0)&x-algolia-application-id=FWTBNXLFS6&x-algolia-api-key=e5fef9eab51259b54d385c6f010cc399'
#url = 'https://api.segment.io/v1/p'
customHead = {
        "Accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "Origin": "https://startupbase.com.br",
        "Referer": "https://startupbase.com.br/",
        "Host": "www.portaltransparencia.gov.br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
    }

data_ajax = '{"requests": \
    [{"indexName":"prod_STARTUPBASE","params":"query=& \
    hitsPerPage=10& \
    maxValuesPerFacet=10& \
    page='+page+'& \
    highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__& \
    facets=%5B%22state%22%2C%22place%22%2C%22group%22%2C%22target%22%2C%22phase%22%2C%22model%22%2C%22badges.badge.name%22%5D&tagFilters=&facetFilters=%5B%5B%22state%3AS%C3%A3o%20Paulo%22%5D%5D"}, \
    { \
    "indexName":"prod_STARTUPBASE", \
    "params":"query=&hitsPerPage=1&maxValuesPerFacet=10&page=0&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=state"}] \
    }'

pg = requests.post(url, headers = customHead, params = query_string, data = data_ajax)
#import pdb; pdb.set_trace()
