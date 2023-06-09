from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

with open('secret.txt', 'r') as file:
	SECRET = file.readline().strip()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'qud1251@likelion.org'
app.config['MAIL_PASSWORD'] = SECRET
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

@app.route('/send-mail', methods=['POST'])
def send_mail():
	if request.method == 'POST':
		spot = request.json.get('spot')
		temperature = request.json.get('temperature')
		humidity = request.json.get('humidity')
		
		recipients = get_recipients()
		msg = Message('Run Away!', sender='qud1251@likelion.org', recipients=recipients)
		msg.body = f"{spot}'s current temperature: {temperature}, humidity: {humidity}!! run away"
		mail.send(msg)
		return 'send mail successfully!'

if __name__ == '__main__':
	app.debug = False # for develop
	app.run(host="127.0.0.1", port="8080")

