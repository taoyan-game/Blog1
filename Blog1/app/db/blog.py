from app.db.mongo import *



def blogContentsNew(blog_context,blog_name,blog_tag,blog_img):
    from app.tools.blog import *
    newblog = blogContentsField()
    blog_max_id = siteContentsField.object.id
    newblogid = blogNewMaxID()
    newblog.id = int(newblogid)
    newblog.name = str(blog_name)
    newblog.contents = str(blog_context)
    newblog.tag = blog_tag
    newblog.img = blog_img
    newblog.save()
    return newblogid


def blogNewMaxID():
    tmp = siteblogContentsField.objects()
    for sc in siteContentsField.objects:
        min_id = sc.BLOG_MIN_ID
        sc.BLOG_MIN_ID += 1
        sc
        return min_id


def blogNewTag(newtags):
    newtag = str(newtags)
    for nt in 

