from flask import Flask, render_template

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#home page
@app.route("/")
def index():

    return render_template("index.html")