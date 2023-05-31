from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'qud1251@likelion.org'
app.config['MAIL_PASSWORD'] = '26294624'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def save_email(email):
	with open('emails.txt', 'a') as file:
		file.write(email + '\n')

def get_recipients():
	recipients = []
	with open('emails.txt', 'r') as file:
		recipients = [line.strip() for line in file]
	return recipients

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		email = request.form.get('email')
		if email:
			save_email(email)
			return 'Email saved successfully!<br/><a href="/">return</a>'
		else:
			return 'Email is required.<br/><a href="/">return</a>'
	return '''
	  <form method="POST" action="/">
		<label for="email">Email</label>
		 <input type="email" id="email" name="email" required>
		 <button type="submit">Submit</button>
	  </form>
	  '''

@app.route('/send-mail')
def send_mail():
	recipients = get_recipients()
	msg = Message('Hello', sender='qud1251@likelion.org', recipients=recipients)
	msg.body = 'Hello Flask message sent from Flask-Mail'
	mail.send(msg)
	return 'send mail successfully!'

if __name__ == '__main__':
	app.debuf = True # for develop
	app.run(host="127.0.0.1", port="8080")

