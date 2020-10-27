from flask import Flask, render_template, request, jsonify
import TestScript
import os
import werkzeug
import cv2
import io
import base64
from PIL import Image

path = "C:/Classnotes/Dress-Virtual-Trialroom/static/"
frontloc = ''
bentloc = ''
backloc = ''
shirtloc = ''
fn = []
app = Flask(__name__)

@app.route("/api",methods=['GET', 'POST'])
def api_call(it):
    files = list(request.files)
    print("Files recieved :",len(files))
    os.chdir(path)
    for file in files:
        image = request.files[file]
        filename = werkzeug.utils.secure_filename(image.filename)
        print(filename)
        abc = filename.split(".")
        print(abc)
        fn.append(str(it) + "." + abc[-1])
        image.save(fn[it-1])
        print("File {} save",it)
    return True


def get_response_image(image_path):
    with open(image_path,"rb") as file:
        content = base64.b64encode(file.read())
        image_base64 = {"base64" : content.decode()}
    return image_base64

def model_test():
    TestScript.start(frontloc, bentloc, backloc, shirtloc)
    encoded = get_response_image(path+"out.jpg")
    return encoded


@app.route("/android", methods=['GET', 'POST'])
def android():
    if api_call(1) == True:
        frontloc = path + fn[0] 
        print("yes")
    if api_call(2) == True:
        bentloc = path + fn[1]
        print("yes")
    if api_call(3) == True:
        backloc = path + fn[2] 
        print("yes")
    if api_call(4) == True:
        shirtloc = path + fn[3]
        print("yes")
    cypher = model_test()
    return jsonify(cypher)

@app.route("/")
def home():
    return "HEllo World"

if __name__ == "__main__":
    app.run()
