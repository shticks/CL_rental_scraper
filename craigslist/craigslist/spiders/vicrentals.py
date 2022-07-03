import scrapy
from ..items import CraigslistItem

class VicrentalsSpider(scrapy.Spider):
    name = 'vicrentals'
    start_urls = [
        'https://victoria.craigslist.org/search/victoria-bc/apa?availabilityMode=0&lat=48.4582&lon=-123.3647&max_price=1650&min_price=&sale_date=all%20dates&search_distance=5'
        ]

    
    def parse(self, response):
        #print("\n")
        #print("HTTP STATUS: " + str(response.status))
        #print(response.css("title::text").get())
        #print("\n")

        allAds = response.css("li.result-row")

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