from flask import Blueprint
from api.module.gmail_sender import GmailSender

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/send_email')
def send_email():
	send_email = GmailSender("qud1251@gmail.com", "0pao0@naver.com", "send_pwd")
	send_email.msg_set("title", "body")
	send_email.smtp_connect_send()
	send_email.smtp_disconnect()

