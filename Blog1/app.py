"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from app import fapp
#app.run(host="0.0.0.0", port=5078, debug=None)

fapp.run()