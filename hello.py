""" Minimal flask app """

from flask import Flask, render_template

# Make the application
app = Flask(__name__)

# Make the route
@app.route("/")

# Now define a function
def hello():
    return render_template('home.html')

# Make a second route
@app.route("/about")

# now make the function w about
def preds():
    return render_template('about.html')
