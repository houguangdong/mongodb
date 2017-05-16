# -*-coding:utf-8-*-
'''
Created on 2017年5月14日

@author: houguangdong
'''

from pymongo import MongoClient
import datetime
import random
import gridfs
from ConfigObject.tests.config import filename


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
# db.blog.find({"comments.name": "bob"}, {"comments.$": 1})

# $eleMatch
# db.blog.find({"x": {"$eleMatch": {"$gt": 10, "$lt": 20}}})
# db.blog.find({"x": {"$gt": 10, "$lt": 20}}).min({"x": 10}).max({"x": 20})

# 查询内嵌文档
# db.hgd.find({"name.first": "hou", "name.last": "dong"})
# db.hgd.find({"comments": {"$elemMatch": {"author": "joe", "score": {"$gte": 5}}}})

# mongod --dbpath  --noscripting

# limit(3)  上限3个
# skip(3)   忽略前3个
# sort("username": 1, "age": -1)  # 1表示升序  -1 表示降序
# 第一页
# db.hgd.find({"describe": "mp3"}).limit(50).sort({"price": -1})
# 第二页
# db.hgd.find({"describe": "mp3"}).limit(50).skip(50).sort({"price": -1})
# db.hgd.find(criteria).limit(100)
# db.hgd.find(criteria).skip(100).limit(100)
# db.hgd.find(criteria).skip(200).limit(100)
# 避免
# var page1 = db.hgd.find().sort({"date", -1}).limit(100)
# var latest = null
# # 显示第一页
# while(page1.hasNext()) {
#     latest = page1.next();
#     display(latest)
# }
# # 获取下一页
# var page2 = db.hgd.find({"date": {"$gt": latest.date}});
# page2.sort({"date": -1}).limit(100);

# 随机一个文档
# db.hgd.insert({"name": "hou", "random": random.random()})
# var random = random.random()
# 随机数比集合中的文档的随机数都大
# result = db.hgd.findOne({"random": {"$gt": random}})
# if (result == null) {
#     result = db.hgd.findOne({"random": {"$lt": random}})
# }

# $maxscan 指定本次查询中扫描文档数量的上限
# db.hgd.find(criteria)._addSpecial("$maxscan", 20)
# $showDiskLoc: true 显示该条结果在磁盘上的位置
# db.hgd.find()._addSpecial("$showDiskLoc", true)

# 快照会使查询变慢     快照用于备份
# db.hgd.find().snapshot()

# 数据库命令
# db.runCommand({"drop": "test"})
# shell 命令
# db.test.drop()
# db.hgd.update({x: 1}, {$inc: {x: 1}}, false, ture)
# 查看数据库中的命令
# db.listCommands()

# 有些命令需要有管理员权限   要在admin数据库上执行
# db.runCommand({"shutdown": 1})

# for(i=0; i<10000; i++) {
#     db.hgd.insert(
#         {
#             "i": i,
#             "username": "user"+i,
#             "age": Math.floor(Math.random() * 120),
#             "created": new Date()
#         }
#     );
# }
# 查看文档的执行过程中所做的事情
# db.hgd.find({"username": "user101"}).explain()
# nscanned 扫描的文档数量
# millis 执行的时间 毫秒数
# n 查询的结果数量
# db.hgd.find({"username": "user101"}).limit(1).explain()

# 创建索引
# db.hgd.ensureIndex({"username": 1})
# db.currentOp()检查mongod的日志查看索引创建的进度
# 查询所用的毫秒数
# db.hgd.find({"username": "user99999"}).explain().millis
# 创建复合索引
# db.hgd.ensureIndex({"age": 1, "username": 1})
# 点查询
# db.hgd.find({"age": 21}).sort({"username": -1})
# 多值查询
# db.hgd.find({"age": {"$gte": 21, "$lte": 30}})
# db.hgd.find({"age": {"$gte": 21, "$lte": 30}}).sort({"username": 1})
# 查看执行步骤
# db.hgd.find({"age": {"$gte": 21, "$lte": 30}}).sort({"username": 1}).explain()
# cursor表示这次查询使用的索引
# scanAndOrder的值是true表示在内存中对数据进行排序
# hint强制mongoDB使用某个特定的索引
# db.hgd.find({"age": {"$gte": 21, "$lte": 30}}).sort({"username": 1}).hint({"username": 1, "age": 1}).explain()
# db.hgd.find({"age": {"$gte": 21, "$lte": 30}}).sort({"username": 1}).limit(1000).hint({"age": 1, "username": 1}).explain()['millis']
# db.hgd.find({"age": {"$gte": 21, "$lte": 30}}).sort({"username": 1}).limit(1000).hint({"username": 1, "age": 1}).explain()['millis']
# 如果在覆盖索引上执行explain() "indexOnly"字段值要为true
# 检查一个键是否存在的查询
# {"key": {"$exists": true}}
# 查询i不等于3的文档
# db.hgd.find({"i": {"$ne": 3}}).explain()
# $not进行反转  {"key": {"$lt": 7}} 变成  {"key": {"$gte": 7}}
# $nin 总是进行全盘扫描
# 查找所有没有"birthday"字段的用户, 用户3月20号新增的用户都有生日字段
# db.hgd.find({"birthday": {"$exists": false}, "_id": {"$lt": march20Id}})

# 范围查找
# db.hgd.find({"age": 47, "username": {"$gt": "user5", "$lt": "user8"}}).explain()
# $or查询
# db.hgd.find({"$or": [{"x": 123}, {"y": 456}]}).explain()
# $in查询无法控制顺序 {"x": [1, 2]}顺序和{"x": [2, 1]}一样

# 索引嵌套文档  查询的文档顺序和子文档顺序一致时，才会用索引
# db.hgd.ensureIndex({"loc.city": 1})

# 索引数组
# db.hgd.ensureIndex({"comments.date": 1})
# db.hgd.ensureIndex({"comments.10.votes": 1})

# 如何索引 {"x": 1, "y": 1}
# db.multi.insert({"x": [1, 2, 3], "y": 1})
# db.multi.insert({"y": [1, 2, 3], "x": 1})
# 非法的
# db.multi.insert({"x": [1, 2, 3], "y": [1, 2, 3]})

# 多键索引的 isMultiKey的值为true
# $natural强制全盘扫描
# db.hgd.find({"created_at": {"$lt": hourAgo}}).hint({"$natural": 1})

# 唯一索引
# db.hgd.ensureIndex({"username": 1}, {"unique": true})
# 复合唯一索引
# db.hgd.ensureIndex({"username": 1, "age": 1}, {"unique": true})
# 去除重复 第一个被保留，之后重复的文档被删除
# db.hgd.ensureIndex({"username": 1}, {"unique": true, "dropDups": true})
# 稀疏索引
# 例如:
# {"_id": 0}
# {"_id": 1, "x": 1}
# {"_id": 2, "x": 2}
# {"_id": 3, "x": 3}
# db.hgd.ensureIndex({"email": 1}, {"unique": true, "sparse": true})
# 返回
# {"_id": 1, "x": 1}
# {"_id": 2, "x": 2}
# {"_id": 3, "x": 3}
# 如何需要那些不包含"x"字段的文档，可以使用hint()强制进行全盘扫描
# 索引的管理
# 所有的数据库索引信息都存储在system.indexs集合中，这是一个保留集合，不能再其中插入和删除文档。只能通过ensureIndex或者dropIndexes对其进行操作
# 创建一个索引之后，就可以在system.indexes中看到它的元信息，可以执行db.collectionName.getIndex()来查看给定集合上的所有索引信息
# 标识索引
# 索引名称的默认形式keyname1_dir1_keyname2_dir2
# keynameX是索引的键  dir1是索引的方向   如: x_1_y_1
# 可以自定义索引的名称
# db.hgd.ensureIndex({"a": 1, "b": 1, "c": 1, ......, "z": 1}, {"name": "alphabet"})
# 调用getLastError可以知道索引是否创建成功或者失败的原因

# 修改索引
# db.hgd.dropIndex("x_1_y_1")
# 如果创建索引 ，或阻塞数据库的读请求和写请求，  如果希望能继续写请求和读请求可以使用background选项
# 在已有的文档上创建索引比新创建索引在插入文档快一点。

# 创建固定集合 10000字节的固定集合 文档数量max等于10
# db.hgd.createCollection("my_collection", {"capped": true, "size": 10000, "max": 10})

# 把普通集合变成固定集合
# db.runCommand({"convertToCapped": "test", "size": 10000})
# 自然排序 $natural
# db.my_collection.find().sort({"natural": -1})
# 没有_id索引的集合
# 如果在调用createCollection创建集合时指定autoIndexId选项为false 此集合不能被复制

# TTL索引 生命周期索引 TTL索引不能是复合索引 可以像普通索引一样排序和查询
# 在ensureIndex中指定expireAfterSecs选项就可以创建一个TTL索引
# db.hgd.ensureIndex({"lastUpdated": 1}, {"expireAfterSecs": 60 * 60 * 24})
# 修改有限期
# db.runCommand({"collMod": "someapp.cache", "expireAfterSecs": 3600})

# 全文本索引
# db.adminCommand({"setParameter": 1, "textSearchEnabled": true})
# 应用
# db.hgd.ensureIndex({"title": "text"})
# db.runCommand({"text": "hn", "search": "ask hn"})
# 一个集合上最多只能有一个全文本索引，但全文本索引可以包含多个字段
# db.hgd.ensureIndex({"title": "text", "desc": "text", "author": "text"})

# 每个字段指定不同的权重来控制不同字段的相对重要性 权重的默认值是1
# db.hgd.ensureIndex({"title": "text", "desc": "text", "author": "text"}, {"weights": {"title": 3, "author": 2}})

# whatever可以指代任何东西，可以使用“$**”在文档的所有字符串字段上创建全文本索引
# db.hgd.ensureIndex({"whatever": "text"}, {"weights": {"title": 3, "author": 1, "$**": 2}})

# 搜索语法
# db.runCommand({text: "hn", search:  "\"ask hn\""})
# 这会精确搜索"ask hn"这个短语，也会可选地搜索"ipod"
# db.runCommand({text: "hn", search:  "\"ask hn\" ipod"})
# db.runCommand({text: "hn", search: "-startup vc"})
# 这样就会返回匹配vc，但是不包含"startup"这个词的文档
# 优化全文本搜索
# 前缀和全文本字段组成的复合索引
# db.hgd.ensureIndex({"date": 1, "post": "text"})
# 后缀和全文本字段组成的复合索引
# db.hgd.ensureIndex({"post": "text", "author": 1})
# db.hgd.ensureIndex({"date": 1, "post": "text", "author": 1})

# 在其他语言中搜索
# db.hgd.ensureIndex({"profil": "text", "interets": "text"}, {"default_language": "french"})
# db.hgd.insert({"username": "hou", "profile": "Bork de bork", language: "swedish"})

# 地理空间索引  2dsphere用于地球表面的地图
# db.world.ensureIndex({"loc": "2dsphere"})

# 地理空间查找的类型
# var eastVillage = {
#     "type": "Polygon", # 多边形
#     "coordinates": [
#         [-73.99999, 40.999999],
#         [-73.8888, 40.88888],
#         [-73.7777, 40.7777],
#         [-73.6666, 40.6666]
#     ]
# }
# db.open.street.map.find({"loc": {"$geoIntersects": {"$geometry": eastVillage}}})
# db.open.street.map.find({"loc": {"$within": {"$geometry": eastVillage}}})
# db.open.street.map.find({"loc": {"near": {"$geometry": eastVillage}}})

# 复合地理空间索引
# db.open.street.map.ensureIndex({"tag": 1, "location": "2dsphere"})
# 可以快速的找到East Village内的披萨店
# db.open.street.map.find({"loc": {"$within": {"$geometry": eastVillage}}, "tags": "pizza"})

# 2d索引
# db.hgd.ensureIndex({"title": "2d"})
# 设置区域大小
# db.hgd.ensureIndex({"light-years": "2d"}, {"min": -1000, "max": 1000})
# db.hgd.find({"tile": {"$near": [20, 21]}}).limit(10)
# db.hgd.find({"tile": {"$within": {"$box": [[10, 20], [15, 30]]}}})
# db.hgd.find({"tile": {"$within": {"$center": [[12, 25], 5]}}})
# db.hgd.find({"tile": {"$within": {"$polygon": [[0, 20], [10, 0], [-10, 0]]}}})

# 使用GridFS存储文件 (以二进制的方式存储大文件)
# echo "Hello world" > foo.txt
# ./mongofiles put foo.txt
# ./mongofiles list
# rm foo.txt
# ./mongofiles get foo.txt
# cat foo.txt
# 还有search和delete操作

# fs = gridfs.GridFS(db)
# file_id = fs.put("Hello world", filename="foo.txt")
# fs.list()
# fs.get(file_id).read()




