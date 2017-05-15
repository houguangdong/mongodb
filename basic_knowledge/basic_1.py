# -*-coding:utf-8-*-
'''
Created on 2017年5月14日

@author: houguangdong
'''

from pymongo import MongoClient
import datetime


client = MongoClient()
db = client.houguangdong

post = {
    "title": "My Blog Post",
    "content": "Here's my blog post.",
    "date": datetime.datetime.now()
}

# db.blog.insert(post)
# print db.blog.find({"title": "My Blog Post"})
# print db.blog.find_one({"title": "My Blog Post"})

# post['comments'] = []
# db.blog.update({"title": "My Blog Post"}, post)
# print db.blog.find_one({"title": "My Blog Post"})

# db.blog.remove({"title": "My Blog Post"})
# print db.blog.find_one({"title": "My Blog Post"})

# mongo ip: port/db

# 客户端不连接任何数据库
# mongo --nodb
# conn = new Mongo("127.0.0.1:27017")
# db = conn.getDB("houguangdong")

# run('ls', 'l')

# mongo --shell .mongorc.js 
# db.dropDatabase()
# 这将删除选定的数据库。如果还没有选择任何数据库，然后它会删除默认的 ' test' 数据库

# db.blog.insert_many([{"1": "1"}, {"2": "2"}, {"3": "3"}])
# print db.blog.find_one({"1": "1"})

# 1 $set
# db.blog.update({"_id" : ObjectId("59172fc00eeb42027cb15bbe")}, {"$set": {"a": "b"}})
# $unset 
# db.blog.update({"_id" : ObjectId("59172fc00eeb42027cb15bbe")}, {"$unset": {"a": "b"}})
# $inc
# db.blog.update({"_id" : ObjectId("59172fc00eeb42027cb15bbe")}, {"$inc": {"score": 50}})
# $push
# db.blog.update({"_id" : ObjectId("59172fc00eeb42027cb15bbe")}, {"$push": {"comments": {"name": "joe", "email": "1737785826@qq.com", "content":"nice post."}}})
# 删除元素 $pull
# db.houguangdong.insert({"todo": ["dished", "laundry", "dry cleaning"]})
# db.houguangdong.update({}, {"$pull": {"todo": "laundry"}})
# update第三个参数表示增加并且更新 第四个参数更新所有的文档

# find() 第一个参数是限定文档，第二个参数是文档的字段
# db.blog.find({}, {"content": "Here's my blog post."})
# 返回的文档中不含“_id”， 含有"username"
# db.blog.find({}, {"username": 1, "_id": 0})

# "lt", "lte", "gt", "gte" < <= > >=
# db.blog.find({"age": {"$gte": 18, "$lte": 30}})
# "$ne" 不等于
# db.blog.find({"username": {"$ne": "joe"}})

# $in  $nin
# db.blog.find({"ticket_no": {"$in": [10, 20, 30]}})
# db.blog.find({"ticket_no": {"$nin": [10, 20, 30]}})

# $or
# db.blog.find({"$or": [{"ticket_no": 725}, {"winner": True}]})

# $mod
# db.blog.find({"id_num": {"$mod": [5, 1]}})
# id_num的值是 1， 6， 11， 16  1/5==1  6／5==1
# $not
# db.blog.find({"id_num": {"not": {"$mod": [5, 1]}}})

# $and
# db.blog.find({"$and": [{"x": 3}, {"x": 4}]})
#$all
# db.blog.find({"fruit": {"$all": ["apple", "banana"]}})
# db.blog.find({"fruit.1", "peach"}) 

# $size
# db.blog.find({"fruit": {"$size": 3}})
# db.blog.update(criteria, {"$push": {"fruit": "strawberry"}, "$inc": {"$size": 1}})

# $slice 返回数组的前几条  23表示数组的偏移位置，10返回的数量
# db.blog.findOne(criteria, {"comments": {"$slice": [23, 10]}})

#返回第一个匹配的文档，第一条评论被返回 
db.blog.find({"comments.name": "bob"}, {"comments.$": 1})

# $eleMatch
db.blog.find({"x": {"$eleMatch": {"$gt": 10, "$lt": 20}}})
db.blog.find({"x": {"$gt": 10, "$lt": 20}}).min({"x": 10}).max({"x": 20})

# 查询内嵌文档
db.hgd.find({"name.first": "hou", "name.last": "dong"})
db.hgd.find({"comments": {"$elemMatch": {"author": "joe", "score": {"$gte": 5}}}})

# mongod --dbpath  --noscripting

# limit(3)  上限3个
# skip(3)   忽略前3个









