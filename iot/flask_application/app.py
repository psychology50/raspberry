from flask import Flask
from .api.routes import api
from .page.routes import page

app = Flask(__name__)

if __name__ == '__main__':
	app.debuf = True # for develop
	app.register_blueprint(api)
	app.register_blueprint(page)
	app.run(host="127.0.0.1", port="80")
