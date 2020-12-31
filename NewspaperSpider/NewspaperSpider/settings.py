# Preset settings for the bot. Inactive options were discarded.

BOT_NAME = "NewspaperSpider"

SPIDER_MODULES = ["NewspaperSpider.spiders"]
NEWSPIDER_MODULE = "NewspaperSpider.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

PROXY_POOL_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    "scrapy_proxy_pool.middlewares.ProxyPoolMiddleware": 610,
    "scrapy_proxy_pool.middlewares.BanDetectionMiddleware": 620,
}

ITEM_PIPELINES = {
   "NewspaperSpider.pipelines.NewspaperSpiderPipeline": 300,
}
