import io
from base64 import encodebytes
from PIL import Image
# from flask import jsonify

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img

# server side code
image_path = 'C:/Classnotes/Dress-Virtual-Trialroom/static/tucked1.jpg' # point to your image location
encoded_img = get_response_image(image_path)
my_message = 'here is my message' # create your message as per your need
response =  { 'Status' : 'Success', 'message': my_message , 'ImageBytes': encoded_img}
print(response)
# return jsonify(response) # send the result to client