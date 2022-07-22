from app.db import blog
from app.db.mongo import blogTagField,blogCategoryField,siteContentsField,blogField





class articles:
    blogallpages = 1
    nowsnumber = 1
    has_next = True 
    has_previous = True
    object_list = []
    def __init__(self,number):
        articles.object_list = blog.queryBlogList(number)
        pages = int(blog.getBlogPages())
        articles.blogallpages = pages
        articles.nowsnumber = number
        if number == pages:
            articles.has_next = False
            articles.has_previous = True
        if number == 1 and pages == 1:
            articles.has_next = False
            articles.has_previous = False
        if number == 1 and pages != 1:
            articles.has_next = True
            articles.has_previous = False
        if number < pages:
            articles.has_next = True
            if number == 1:
                articles.has_previous = False
            else:
                articles.has_pervious = True

class randomclass():
    num = 1
    def __init__(self,id):
        num = 1
    def num(self,start,end):
        import random
        num = random.random(start,end)
        randomclass.num = num
        return num





class tagclass:
    id = 1
    name = ""
    has_this_article = 1
    def __init__(self,id):
        tagclass.id = id
        for i in blogTagField.objects(tagid=id):
            tagclass.name = i.tagname
            tagclass.has_this_article = blogField.objects(id).all().count()



class categoryclass:
    id = 1
    name = ""
    has_this_article = 1
    def __init__(self,id):
        categoryclass.id=id
        for i in blogCategoryField.objects(categoryid=id):
            categoryclass.name = i.categoryname
            categoryclass.has_this_article = blogCategoryField.objects(id).all().count()


class siteclass:
    #SITE_URL = ""
    #STIE_TITLE = ""
    #SITE_ICP = ""
    #SITE_START_TIME = ""
    #SITE_MAIL = ""
    #SITE_YEAR = ""
    #SITE_AVATAR = ""
    #BeautifulSentence = ""
    #SITE_TYPE_ENGLISH = ""
    #SITE_TYPE_CHINESE = ""
    def __init__(self):
        for i in siteContentsField.objects(objectsid=1):
            siteclass.SITE_URL = i.SITE_URL
            siteclass.SITE_TITLE = i.SITE_TITLE
            siteclass.SITE_ICP = i.SITE_ICP
            siteclass.SITE_START_TIME = i.SITE_START_TIME
            siteclass.SITE_MAIL = i.SITE_MAIL
            siteclass.SITE_YEAR = i.SITE_YEAR
            siteclass.SITE_AVATAR = i.SITE_AVATAR
            siteclass.BeautifulSentence = i.BeautifulSentence
            siteclass.SITE_TYPE_ENGLISH = i.SITE_TYPE_ENGLISH
            siteclass.SITE_TYPE_CHINESE = i.SITE_TYPE_CHINESE

class blogdetial:
    bid = 100000000
    btag = []
    bcategory = categoryclass
    bdate = ""
    btitle = ""
    bcontents = ""
    bimg = ""
    bdesc = ""
    bclick_count = 1


    def __init__(self,id,taglist,category,date,title,contents,img,desc):
        self.bid = id
        self.btag = taglist
        self.bcategory = category
        self.bdate = date
        self.btitle = title
        self.bcontents = contents
        self.bimg = img
        self.bdesc = desc



class TagArticles:
    blogallpages = 1
    nowsnumber = 1
    has_next = True 
    has_previous = True
    has_this_article = 0
    object_list = []
    def __init__(self,number,id):
        TagArticles.object_list = blog.queryBlogListFromTag()
        lisa = [id]
        pages = int(blogField.objects(blogtag__in=lisa).all().count())
        mo = pages / 9
        mt = pages // 9
        if pages < 9:
            TagArticles.blogallpages = 1
        else:
            if mo > mt:
                i = mt + 1
                TagArticles.blogallpages = i
            else:
                TagArticles.blogallpages = mt
        TagArticles.has_this_article = pages
        TagArticles.nowsnumber = number
        if number == pages:
            CateArticles.has_next = False
            CateArticles.has_previous = True
        if number == 1 and pages == 1:
            CateArticles.has_next = False
            CateArticles.has_previous = False
        if number == 1 and pages != 1:
            CateArticles.has_next = True
            CateArticles.has_previous = False
        if number < pages:
            CateArticles.has_next = True
            if number == 1:
                CateArticles.has_previous = False
            else:
                CateArticles.has_pervious = True

class CateArticles:
    blogallpages = 1
    nowsnumber = 1
    has_next = True 
    has_previous = True
    has_this_article = 0
    object_list = []
    def __init__(self,number,id):
        CateArticles.object_list = blog.queryBlogListFromCate()
        lisa = [id]
        pages = int(blogField.objects(blogcategory=lisa).all().count())
        mo = pages / 9
        mt = pages // 9
        if pages < 9:
            CateArticles.blogallpages = 1
        else:
            if mo > mt:
                i = mt + 1
                CateArticles.blogallpages = i
            else:
                CateArticles.blogallpages = mt
        CateArticles.has_this_article = pages
        CateArticles.nowsnumber = number
        if number == pages:
            CateArticles.has_next = False
            CateArticles.has_previous = True
        if number == 1 and pages == 1:
            CateArticles.has_next = False
            CateArticles.has_previous = False
        if number == 1 and pages != 1:
            CateArticles.has_next = True
            CateArticles.has_previous = False
        if number < pages:
            CateArticles.has_next = True
            if number == 1:
                CateArticles.has_previous = False
            else:
                CateArticles.has_pervious = True