import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret phrase being secret')


###
# Routing for your application.
###


if __name__ == '__main__':
    app.run(debug=True)
