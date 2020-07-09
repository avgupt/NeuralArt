from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import flask_SQLAlchemy 

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////images.db'
#db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', methods = ['GET', 'POSTS'])

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/stylize')
def stylize():
	return render_template('stylize.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')
	
if __name__ == "__main__":
	app.run(debug=True)