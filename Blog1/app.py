"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from app import app
from tornado import httpserver
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler
from tornado.web import Application


app.config['SECRET_KEY']='taoyanmua;;sbhacker才会爆破密码;;sbhackeronlyhavepasswd'
app.debug = True
application = httpserver(WSGIContainer(app))
https_cert_file = r"cert.pem"
https_key_file = r"cert.key"
server = HTTPServer(application, ssl_options={"certfile": https_cert_file, "keyfile": https_key_file})
server.listen(443)
IOLoop.instance().start()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090)
