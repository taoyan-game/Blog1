from flask import Flask

fapp = Flask(__name__)

import app.home.views
import app.tools.request