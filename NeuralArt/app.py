from flask import Flask, render_template, url_for, request, redirect

import tensorflow_hub as hub

import tensorflow as tf

import matplotlib.pyplot as plt
import uuid
import numpy as np

import PIL.Image as Image

import IPython.display as display

from flask import Flask, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename 

import os
import glob

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


def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return Image.fromarray(tensor)

def model(content, style):
  global transformed

  content_image_path = 'static/' + content + '.jpg'
  style_image_path = 'static/' + style + '.jpg'


  # Load content and style images (see example in the attached colab).
  content_image = plt.imread(content_image_path)
  style_image = plt.imread(style_image_path)

  os.remove(content_image_path)
  os.remove(style_image_path)

  # Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
  content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
  style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
  style_image = tf.image.resize(style_image, (256, 256))

  # Load image stylization module.
  hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

  # Stylize image.
  outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
  stylized_image = outputs[0]
  transformed = str(uuid.uuid4())

  tensor_to_image(stylized_image).save("static/" + transformed + '.jpg')
  return transformed


def makevar():
  import uuid
  content = str(uuid.uuid4())
  style = str(uuid.uuid4())
  return content, style

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

    return render_template('result.html', filename=fname)
    #return render_template('stylize.html')

	
if __name__ == "__main__":
	app.run(debug=True)
