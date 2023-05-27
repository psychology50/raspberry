from flask import Flask
from .module.gmail_sender import GmailSender

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World!"

@app.route('/send_email')
def send_email():
	send_email = GmailSender("sender_email", "receiver_email", "sender_pwd")
	send_email.msg_set("title", "body")
	send_email.smtp_connect_send()
	send_email.smtp_disconnect()

if __name__ == '__main__':
	app.debuf = True # for develop
	app.run(host="127.0.0.1", port="80")
