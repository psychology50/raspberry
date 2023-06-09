import smtplib
from email.message import EmailMessage

class GmailSender:
	def __init__(self, sender_email, receiver_email, sender_pwd, cc_email = "", bcc_email = ""):
		self.s_email = sender_email
		self.r_email = receiver_email
		self.pw = sender_pwd
		self.server_name = "smtp.gmail.com"
		self.server_port = 587

		self.msg = EmailMessage()
		self.msg["From"] = self.s_email
		self.msg["To"] = self.r_email

		if cc_email != "":
			self.cc_email = cc_email
			self.msg["Cc"] = self.cc_email
		if bcc_email != "":
			self.bcc_email = bcc_email
			self.msg["Bcc"] = self.bcc_email
		self.smtp = smtplib.SMTP(self.server_name, self.server_port)

	def msg_set(self, msg_title, msg_body):
		self.msg["Subject"] = msg_title
		self.msg.set_content(msg_body)

	def smtp_connect_send(self):
		self.smtp.ehlo()
		self.smtp.starttls()
		self.smtp.login(self.s_email, self.pw)
		self.smtp.send_message(self.msg)

	def smtp_disconnect(self):
		self.smtp.close()
