from flask import Flask, render_template
import TestScript
import os
import openpose_model
import cv2

path = "C:/Classnotes/Dress-Virtual-Trialroom/static/"
frontloc = "C:/Classnotes/Dress-Virtual-Trialroom/tucked1.jpg"
bentloc = "C:/Classnotes/Dress-Virtual-Trialroom/tucked2.png"
backloc = "C:/Classnotes/Dress-Virtual-Trialroom/tucked3.png"
shirtloc = "C:/Classnotes/Dress-Virtual-Trialroom/transparent1.png"


app = Flask(__name__)

@app.route("/index", methods=['GET', 'POST'])
def out():
    TestScript.start(frontloc, bentloc, backloc, shirtloc)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()