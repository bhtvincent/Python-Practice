# ----------------------------------------------------------------------
# Name:        lecture27a
# Purpose:     Demonstrate web development with Flask
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing a starter web application to be used in lecture 27.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000
"""
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def welcome():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

def main():
    app.run(debug = True)

if __name__ == "__main__":
    main()
