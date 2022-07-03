import scrapy
from ..items import CraigslistItem


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    start_urls = [
        'https://newyork.craigslist.org/d/real-estate/search/rea'
    ]

    def parse(self, response):
        #print("\n")
        #print("HTTP STATUS: " + str(response.status))
        #print(response.css("title::text").get())
        #print("\n")

        allAds = response.css("div.result-info")

        for ad in allAds:
            date = ad.css("time::text").get()
            title = ad.css("a.result-title.hdrlnk::text").get()
            price = ad.css("span.result-price::text").get()
            link = ad.css("a::attr(href)").get()

            items = CraigslistItem()
            
            items['date'] = date
            items['title'] = title
            items['price'] = price
            items['link'] = link

            yield items