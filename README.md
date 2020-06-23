# NeuralArt 
A simple web application implements style transfer

## Group 38
Avishi, Vaseem Naazleen, Shivangi Tomar

## Neural Style Transfer
Neural style transfer is an optimization technique takes two images 
* A content image 
* A style reference image (such as an artwork by a famous painter) 
and blend them together so the output image looks like the content image, but  “painted” in the style of the style reference image.
* Gatys et al(A Neural Algorithm of Artistic Style) introduced a way to use Convolutional Neural Network (CNN) to separate and recombine the image content and style of natural images by extracting image representations from response layers in VGG networks.

The below shows how it looks :

![nst](https://user-images.githubusercontent.com/54474853/85428391-c13fdb00-b59a-11ea-9769-01affe0839ec.png)

### Examples of Neural Style transfer

* A - Content Image
* B, C, D, E, F - Stylized Images (Style Image at Right corner)

![examples](https://user-images.githubusercontent.com/54474853/85428804-5fcc3c00-b59b-11ea-9383-ae4a86f42925.jpeg)

## How the Web App works?
Steps to follow to convert your image into stylized image in our NeuralArt web app :
1. **UPLOAD IMAGE**           :- Upload your image which is to converted (Content Image)
2. **SELECT OR UPLOAD IMAGE** :- Select the style image from the provided style images or Upload your own style images
3. **CLICK CREATE**           :- Your image will be stylized.

## Tech stuff to be used :
* Tensorflow (To stylize the image)
* django or flask (To build the web app)
## REFERENCES :
* [Wikipedia NST](https://en.wikipedia.org/wiki/Neural_Style_Transfer#NST)
* [A Neural Algorithm of Artistic Style (Gatys et al.)](https://arxiv.org/abs/1508.06576)
* [TensorFlow NST Tutorial](https://www.tensorflow.org/tutorials/generative/style_transfer)
## Extenstion Aimed to be done in future:

Extend the web application to stylize videos

