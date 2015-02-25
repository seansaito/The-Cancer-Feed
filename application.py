from os import environ

from app import application

if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    application.run(debug=True, port=port, processes=2)
