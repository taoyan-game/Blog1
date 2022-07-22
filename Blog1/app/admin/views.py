from app import fapp
from app.db.mongo import blogAdminField
from app.admin.forms import AdminLoginForm
from app.admin import db
from flask import render_template
from flask import session
from flask import redirect




@fapp.route("/xxxx/admin/login/",methods=["GET","POST"])
def AdminLoginView():
    loginform = AdminLoginForm()
    data = {}
    if loginform.validate_on_submit():
        data["name"] = loginform.name.data
        data["password"] = loginform.password.data
        data["remberme"] = loginform.remberme.data
        if db.checkadmin(loginform.name.data,loginform.password.data):
            session["adminid"] = db.getAdminID(loginform.password.data)
            return redirect(redirect("/"+getAdminSecretRoute()+"/home/"))
        else:
            return render_template(
            "admin/login.html",
            loginform=loginform
            )
    else:
        return render_template(
            "admin/login.html",
            loginform=loginform
            )

@fapp.route("/<secret_key>/home/")
@db.checkAdmin
def AdminHomwView(secret_key):
    if secret_key == db.getAdminSecretRoute():
        adminsite = db.adminsite("home")
        return render_template(
            "admin/home.html",
            adminsite=adminsite,
            adminname=db.getAdminName()
            )
    else:
        return redirect("/errorpage")

@fapp.route("/<secret_key>/tag-manager/")
@db.checkAdmin
def AdminTagView(secret_key):
