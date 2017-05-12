# -*-coding:utf-8-*-
'''
Created on 2017年5月12日

@author: ghou
'''

import datetime
from pymongo import MongoClient
from mongoengine import *


# client = MongoClient()
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017')

# db = client.pymongo_test
# db = client['pymongo_test']

# 集合相当于表
# posts = db.posts
# 文档相当于行
# 插入1行
# post_data = {
#   'title': 'Python and MongoDB',
#   'content': 'PyMongo is fun, you guys',
#   'author': 'Scott'
# }
# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))

# 插入多行
# post_1 = {
#   'title': 'Python and MongoDB',
#   'content': 'PyMongo is fun, you guys',
#   'author': 'Scott'
# }
# post_2 = {
#   'title': 'Virtual Environments',
#   'content': 'Use virtual environments, you guys',
#   'author': 'Scott'
# }
# post_3 = {
#   'title': 'Learning Python',
#   'content': 'Learn Python, it is easy',
#   'author': 'Bill'
# }
# new_result = posts.insert_many([post_1, post_2, post_3])
# print('Multiple posts: {0}'.format(new_result.inserted_ids))

# bills_post = posts.find_one({'author': 'Bill'})
# print(bills_post)
# 
# scotts_posts = posts.find({'author': 'Scott'})
# print(scotts_posts)
# for post in scotts_posts:
#     print(post)

# 和pymongo不同。MongoEngine需要制定数据库名称。
connect('mongoengine_test', host='localhost', port=27017)

 
class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

post_1 = Post(
  title='Sample Post',
  content='Some engaging content',
  author='Scott'
)
post_1.save()    # This will perform an insert
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()    # This will perform an atomic edit on "title"
print(post_1.title)


# class Post1(Document):
#     title = StringField()
#     published = BooleanField()
#     @queryset_manager
#     def live_posts(self, clazz, queryset):
#         return queryset.filter(published=True)


# class Author(Document):
#     name = StringField()
# 
#  
# class Post2(Document):
#     author = ReferenceField(Author)
# 
# Post.objects.first().author.name