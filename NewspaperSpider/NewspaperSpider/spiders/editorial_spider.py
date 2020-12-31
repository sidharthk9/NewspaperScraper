import scrapy
from ..items import LinkItem


class EditorialSpider(scrapy.Spider):
    name = "EditorialSpider"
    pageLink = 2
    pageLimit = 1000
    incompleteUrl = []

    def start_requests(self):
        urls = ["https://www.khaleejtimes.com/editorials-columns&pagenumber=1", ]
        for link in urls:
            yield scrapy.Request(url=link, callback=self.url_collection)

    def url_collection(self, response):
        listElement = response.css(" .liting_list")
        self.incompleteUrl = listElement.css(" h2 a::attr(href)").extract()

        finalUrl = []
        for link in self.incompleteUrl:
            finalUrl.append("https://www.khaleejtimes.com" + link)

        for link in finalUrl:
            yield scrapy.Request(url=link, callback=self.parse)

        nextPage = "https://www.khaleejtimes.com/editorials-columns&pagenumber="+str(self.pageLink)
        if self.pageLink <= self.pageLimit:
            self.pageLink += 1
            yield response.follow(nextPage, callback=self.url_collection)

    def parse(self, response):
        items = LinkItem()
        items["article"] = response.css(" .articlepage_content_zz > p::text").extract()
        yield items
