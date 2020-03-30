import os
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#home page
@app.route("/")
def index():

    return render_template("index.html")

#gallery
@app.route("/slideshow/<attribute>")
def slideshow(attribute):
    #get name of requested image directory in /images and respond with images within
    projects = os.listdir('static/images')

    if (attribute in projects):
        images = os.listdir(f'static/images/{attribute}')
        
        return jsonify({"success": True, "project": images})

    else:
        return jsonify({"success": False})