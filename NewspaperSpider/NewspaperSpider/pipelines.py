import pymongo  # MongoDB database wrapper for python
import config


class NewspaperSpiderPipeline(object):

    def __init__(self):
        self.connection = pymongo.MongoClient(config.MongoDbConnectionString)
        db = self.connection["tpTimes"]
        self.collection = db["opinion"]

    def process_item(self, item, spider):
        return item
