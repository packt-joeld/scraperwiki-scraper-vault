import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://scraperwiki.com/")
root = lxml.html.fromstring(html)

for el in root.cssselect("div.footer_inner"):
print el


import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://scraperwiki.com/")
root = lxml.html.fromstring(html)

for el in root.cssselect("div.footer_inner"):
print el


