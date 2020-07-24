from flask import Flask, render_template, url_for, request, redirect


from flask import Flask, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename 

from functions import *


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', methods = ['GET', 'POSTS'])

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/stylize')
def to_upload_page():
    return render_template('stylize.html')


@app.route('/uploader', methods=['POST'])
def file_upload():
    
    
    content, style = makevar()

    content_file = request.files['contentFile']
    style_file = request.files['styleFile']

    try:
      if content_file and style_file:
        content_file.save('static/' + content + '.jpg')
        style_file.save('static/' + style + '.jpg')
        transformed = model(content, style)
      
        fname = transformed + '.jpg'

    except:

        fname = 'error.jpg'

    delete_files()
        
    return render_template('result.html', filename=fname)
	

if __name__ == "__main__":
	app.run(debug=True)
