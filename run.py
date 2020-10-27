from flask import Flask, render_template, request, jsonify
import TestScript
import os
import werkzeug
import cv2
import io
from base64 import encodebytes
from PIL import Image

path = "C:/Classnotes/Dress-Virtual-Trialroom/static/"

fn = []
app = Flask(__name__)

@app.route("/api",methods=['GET', 'POST'])
def api_call():
    files = list(request.files)
    print("{} Files recieved",len(files))
    it=1
    os.chdir(path)
    for file in files:
        print("\nSaving Image No. ", str(it), "/", len(files))
        image = request.files[file]
        filename = werkzeug.utils.secure_filename(image.filename)
        filename.split(".")
        fn[it-1] = str(it) + "." + filename[-1]
        image.save(fn[it-1])
        print("File {} save",it)
        it = it + 1
    return True

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    tup = {"base64" : encoded_img}
    return tup



@app.route("/", methods=['GET', 'POST'])
def home():
    if api_call() == True:
        frontloc = path + fn[0] 
        bentloc = path + fn[1]
        backloc = path + fn[2] 
        shirtloc = path + fn[3]
        TestScript.start(frontloc, bentloc, backloc, shirtloc)
        encoded = get_response_image(path+"out.jpg")
        return jsonify(encoded)
    return jsonify("error")



if __name__ == "__main__":
    app.run()