from flask import Blueprint

page = Blueprint('page', __name__)

@page.route('/')
def hello():
	return "Hello, World!"