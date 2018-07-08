#!/usr/bin/python
#

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['python']
collection = db['training']

import datetime
post = {"author": "AP2V Solutions", "text": "Python Advance Training", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
#posts = db.posts
posts = db['training']
post_id = posts.insert_one(post).inserted_id
print post_id
posts.find_one({"author": "AP2V Solutions"})
posts.find_one({"_id": post_id})

new_posts = [{"author": "AP2V Solutions", "text": "Sample Post", "tags": ["bulk", "insert"], "date": datetime.datetime(2009, 11, 12, 11, 14)}, {"author": "Ashutosh Taiwal", "title": "Python Mongo Insert Many Example", "text": "Another Sample Entry", "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
result.inserted_ids

posts.find({"author": "AP2V Solutions"}).count()

