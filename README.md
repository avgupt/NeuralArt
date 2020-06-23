# NeuralArt 
A simple web application implements style transfer

## Group 38
Avishi, Vaseem Naazleen, Shivangi Tomar

## Neural Style Transfer
Neural style transfer is an optimization technique takes two images 
* a content image 
* a style reference image (such as an artwork by a famous painter) 
and blend them together so the output image looks like the content image, but  “painted” in the style of the style reference image.
* A Neural Algorithm of Artistic Style that can separate and recombine the content and style of natural images.

The below shows how it looks :

![nst](https://user-images.githubusercontent.com/54474853/85428391-c13fdb00-b59a-11ea-9769-01affe0839ec.png)

### Examples of Neural Style transfer

![examples](https://user-images.githubusercontent.com/54474853/85428804-5fcc3c00-b59b-11ea-9383-ae4a86f42925.jpeg)

## How the Web App works?
Steps to follow to convert your image into stylized image in our NeuralArt web app :
* UPLOAD IMAGE           :- Upload your image which is to converted (Content Image)
* SELECT OR UPLOAD IMAGE :- Select the style image from the provided style images or Upload your own style images
* CLICK CREATE           :- Your image will be stylized.

## Tech stuff to be used :
* Tensorflow (To stylize the image)
* django or flask (to build the web app)

## Extenstion Aimed to be done in future:

Extend the web application to stylize videos

