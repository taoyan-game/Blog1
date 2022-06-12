from mongoengine import *
connection.connect("blog",host="localhost",port=27017,name="taoyan",password="Qwe123./")
#连接mongo


class blogContentsField(Document): #博客内容的Model类
    id = IntField(min_value=100000000,max_value=205509722,required=True)#max_value是我的原神UID,天空岛
    name = StringField(max_length=50)
    contents = StringField()
    tag = ListField(field=blogTagField)
    img = ReferenceField(assetsField)

class blogListField(Document): #博客文章的列表
    list = ListField(field=IntField())

class blogTagField(Document): #博客的标签Model类
    tag = StringField()
    
class blogTagListField(Document):
    tagList = ListField(field=blogTagField)

class assetsField(Document): #各种资源(如标题图片，文件什么的。只保存索引)
    route = StringField(max_length=10000)
    place = StringField(max_length=20)#这个是保存的地方，如有的是放在了static/staticfile,有的是标题图片，有的是博客里的图片

class blogAdminListField(Document): #博客管理员的列表
    adminlist = ListField(field=StringField())

class blogAdminField(Document): #博客的管理员信息
    adminname = StringField()
    adminpwd = StringField()
    adminimg = ReferenceField(assetsField)
    adminid = IntField()

class siteContentsField(Document): #杂项信息
    id = 1 #单纯用于查找
    SITE_URL = StringField()
    STIE_NAME = StringField()
    BLOG_MIN_ID = IntField(min_value=100000000)
