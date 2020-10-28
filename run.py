from flask import Flask, render_template, request, jsonify
import TestScript
import os
import json
import werkzeug
import cv2
import io
import base64
import time
from PIL import Image

path = "C:/Classnotes/Dress-Virtual-Trialroom/static/"
fn = []
app = Flask(__name__)


def get_response_image(image_path):
    with open(image_path,"rb") as file:
        content = base64.b64encode(file.read())
        image_base64 = {"base64" : content.decode()}
    return image_base64


def deleting_files():
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))

'''
@app.route("/colour-blind",methods=['GET', 'POST'])
def blindness(error):
    if error == "P":
        #call function using import and rewrite the changes in out.jpg
    elif error == "D":
        #call function using import rewrite the changes in out.jpg
    elif error == "T":
        #call function using import rewrite the changes in out.jpg
    return'''


def model_run(error):
    frontloc = path + fn[0]
    bentloc = path + fn[1]
    backloc = path + fn[2]
    shirtloc = path + fn[3]
    TestScript.start(frontloc, bentloc, backloc, shirtloc)
    #blindness(error)
    encoded = get_response_image(path+"waka.jpg")
    return encoded


@app.route("/api/android",methods=['GET', 'POST'])
def api_call():
    incoming_files = list(request.files)
    print("Files recieved :",len(incoming_files))
    os.chdir(path)
    it = 1
    error = 'N'
    for file in incoming_files:
        image = request.files[file]
        filename = werkzeug.utils.secure_filename(image.filename)
        print()
        print(filename)
        abc = filename.split(".")
        if abc[-1] != "json":    
            fn.append(str(it) + "." + abc[-1])
            image.save(fn[it-1])
        else:
            error = json.loads(filename.decode())
        print("File saved ",it)
        it = it + 1
    cypher = model_run(error)
    #deleting_files()
    return jsonify(cypher)


@app.route("/", methods=['GET', 'POST'])
def home():
    return "HEllo World"


if __name__ == "__main__":
    app.run()
