from flask import render_template
from flask import Request
from flask import redirect
from flask import url_for
from app import fapp
from app.db.blog import *
from app.db.blogclass import articles,randomclass
from app.db.blogclass import articles,randomclass
from app.tools.request import *
import random

@fapp.route("/")
@fapp.route("/home/")
def HomeView():
    if checkRequest():
        top_articles = queryrecommendblog()
        all_articles = articles(1)
        site = getSite()
        allpages = blog.getBlogPages()
        return render_template(
            "index.html",
            site = site,
            all_articles=all_articles,
            top_articles=top_articles
        )
    else:
        return "sb"

@fapp.route("/archive/")
def ArchiveFView():
    if checkRequest():
        all_articles = articles(number=int(1))
        site = getSite()
        return render_template(
            "archive.html",
            site=site,
            all_articles=all_articles
            )
    else:
        return "sb"

@fapp.route("/archive/page/<int:nowsnumber>/")
def ArchiveView(nowsnumber):
    if checkRequest():
        allpages = blog.getBlogPages()
        if allpages >= nowsnumber:
            all_articles = articles(number=int(nowsnumber))
            site = getSite()
            return render_template(
                "archive.html",
                site=site,
                all_articles=all_articles
                )
        else:
            return render_template("404.html"),404
    else:
        return "sb"



@fapp.route("/article/id/<id>/")
def ArticleView(id):
    if checkRequest():
        site = getSite()
        article = queryapost(int(id))
        return render_template(
            "article.html",
            site=site,
            article=article
            )
    else:
        return "sb"

@fapp.route("/tag/")
def TagView():
    if checkRequest():
        site = getSite()
        tags = getaTagList()
        randomclass= randomclass()
        return render_template(
            "tag.html",
            site=site,
            tags=tags,
            randomclass=randomclass
            )

@fapp.route("/tag/id/<tagid>/article/page/<pages>")
def TagArticleView(tagid,pages):
    site = getSite()
    tags = getaTagList()
    randomclass = randomclass()
    article = TagArticles(pages,tagid)
    return render_template(
        "article_tag.html",
        site=site,
        tags=tags,
        randomclass=randomclass,
        article=article
        )

@fapp.route("/category/")
def CategoryView():
    if checkRequest():
        site = getSite()
        categories = getaCategoryList()
        return render_template(
            "category.html",
            site=site,
            categories=categories
            )

@fapp.route("/category/id/<cateid>/article/page/<pages>/")
def CategoryArticleView(cateid,pages):
    site = getSite()
    categories = getaCategoryList()
    randomclass = randomclass()
    article = CateArticles(pages,cateid)
    return render_template(
        "article_tag.html",
        site=site,
        categories=categories,
        randomclass=randomclass,
        article=article
        )

@fapp.route("/about/")
def AboutView():
    site=getSite()
    return render_template(
        "about.html"
        )

@fapp.errorhandler(404)
@fapp.errorhandler(505)
@fapp.route("/errorpage")
def ErrorView(err):
    return render_template("404.html"),404

@fapp.route("/test/addtag<name>")
def createatesttag(name):
    blogNewTag(name)
    return name

@fapp.route("/test/addcategory<name>")
def createatestcategory(name):
    id = blogNewCategory(name)
    return id

@fapp.route("/test/addblog<title>/<tag>/<category>/<img>/<isre>/<desc>/")
def createatestblog(title,tag,category,img,isre,desc):
    blogContentsNew(blog_context="I am using __markdown__.",blog_title=title,blog_tag=[tag],blog_category_id=category,blog_img=img,blog_is_recommend=isre,blog_desc=desc)
    return "ok"
    
@fapp.route("/test/addblog/")
def abab():
    blogtestsitecontents()
    return "ok"

