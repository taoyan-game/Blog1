from app.db import mongo
from flask import session
from flask import redirect
from app.db import blogclass
import functools



def checkadmin(name,pwd):
    try:
        for tmp in blogAdminField.objects(adminname=name):
            pwdhash = tmp.adminpwd
            if check_password_hash(pwdhash,pwd):
                return True
            else:
                return False
    except Exception as e:
        return False
    finally:
        return False

def getAdminSecretRoute():
    d = ""
    for i in mongo.siteContentsField.objects(objectsid=1):
        d = i.secret_route
    return d

def getAdminID(name):
    id = 1
    for i in mongo.blogAdminField.objects(adminname=name):
        id = i.adminid
    return id

def idInAdmin(id):
    try:
        for i in mongo.blogAdminField.objects(adminid__in=[id]):
            return True
    except Exception:
        return False

def checkAdmin(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        if "adminid" in session:
            return redirect("/"+getAdminSecretRoute()+"/home/")
        return func(*args,**kwargs)
    return inner

def getAdminName():
    name = ""
    for i in mongo.blogAdminField(adminid=session.get(adminid)):
        name = i.adminname
    return name

class adminsite:
    def __init__(self,where):
        for i in mongo.siteContents.objects(objectsid=1):
            self.sitename = i.SITE_TITLE
            self.secret_route = i.secret_route
            self.year = i.SITE_YEAR
        if where == "home":
            self.page_home = True
        elif where == "post":
            self.page_post = True
        elif where == "tag":
            self.page_tag = True
        elif where == "category":
            self.page_category = True
        elif where == "admin":
            self.page_admin = True
        else:
            self.page_other = True

def getAdminTagList():
    taglista = []
    tagcount = mongo.blogTagField.objects.all().count()
    s = tagcount/9
    d = tagcount//9
    if s > d:
        s = d+1
    for i in range(0,)
    for i in mongo.blogTagField.objects.all():
        taglista.append(blogclass.tagclass(i.tagid))
    