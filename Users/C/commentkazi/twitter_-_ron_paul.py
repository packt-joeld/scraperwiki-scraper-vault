# Blank Python
###############################################################################
# Twitter srcaper for the term 'Stadswarmte'.
###############################################################################

import scraperwiki
import simplejson

# retrieve a page
base_url = 'http://search.twitter.com/search.json?q='
q = 'Stadswarmte'
options = '&rpp=100&page='
page = 1

while 1:
    try:
        url = base_url + q + options + str(page)
        html = scraperwiki.scrape(url)
        #print html
        soup = simplejson.loads(html)
        for result in soup['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            # save records to the datastore
            scraperwiki.sqlite.save(["id"], data) 
        page = page + 1
    except:
        print str(page) + ' pages scraped'
        break
        
    # Blank Python
###############################################################################
# Twitter srcaper for the term 'Stadswarmte'.
###############################################################################

import scraperwiki
import simplejson

# retrieve a page
base_url = 'http://search.twitter.com/search.json?q='
q = 'Stadswarmte'
options = '&rpp=100&page='
page = 1

while 1:
    try:
        url = base_url + q + options + str(page)
        html = scraperwiki.scrape(url)
        #print html
        soup = simplejson.loads(html)
        for result in soup['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            # save records to the datastore
            scraperwiki.sqlite.save(["id"], data) 
        page = page + 1
    except:
        print str(page) + ' pages scraped'
        break
        
    