from flask import Blueprint, render_template
import models

app = Blueprint('index', __name__)

@app.route('/')
def index():
    html_main = "You Can View Table views."
    list_Tests = models.Test.query.all()
    return render_template('index.html', page_title="View", html_main=html_main, lists=list_Tests)
