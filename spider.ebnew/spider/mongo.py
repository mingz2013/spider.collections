# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import random

# MONGO
# MONGO_URI = "localhost:27017"
# mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_client = pymongo.MongoClient()

ebnew_db = mongo_client["ebnew"]


class EbnewDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(company):
        logging.info("<MONGO> %s" % company)
        ebnew_db.company_info.update({u'url': company[u'url']}, {'$set': company}, True, True)

    @staticmethod
    def find_one(url):
        logging.info("<MONGO> %s" % url)
        company = ebnew_db.company_info.find_one({u'url': url})
        if company:
            return True
        else:
            return False
