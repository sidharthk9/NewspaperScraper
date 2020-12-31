import scrapy
from ..items import TitleItem


class TitleSpider(scrapy.Spider):
    name = "TitleSpider"
    pageNumber = 2

    def start_requests(self):
        urls = ["https://www.khaleejtimes.com/news&pagenumber=1", ]
        for link in urls:
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        items = TitleItem()

        listElement = response.css(" .liting_list")
        for titleTag in listElement:
            items["heading"] = titleTag.css("h2 a::text").extract()
            yield items

        nextPage = "https://www.khaleejtimes.com/news&pagenumber="+str(self.pageNumber)
        if self.pageNumber <= 178:
            self.pageNumber += 1
            yield response.follow(nextPage, callback=self.parse)
