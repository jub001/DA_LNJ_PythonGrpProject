import requests

url = 'http://172.18.58.80/index.php'
r = requests.get(url)
print("Get:", r.text)

print("Status Code:")
print("\t *", r.status_code)
# HTTP response code 200 -> OK

hurl = 'http://172.18.58.80/headers.php'
h = requests.head(hurl)
print("Headers")
print("****")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("****")

headers = {
    'User-Agent': 'Mobile'
}

rh = requests.get(hurl, headers=headers)
print(rh.text)

import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/index.html']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield{
                'Image Link':x.xpath(newsel).extract_first(),
            }

class NewSpider(scrapy.Spider):
    name= "new_spider"
    start_urls = ['http://172.18.58.80/index.html']
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

import unittest

class Task8(unittest.TestCase):

    def test_EngineType(self):
        print("Testing")

if __name__ == '__main__':
    unittest.main()