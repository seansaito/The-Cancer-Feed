from os import environ

from app import application
application.run(debug=True, port=environ.get("PORT", 5000), processes=2)
