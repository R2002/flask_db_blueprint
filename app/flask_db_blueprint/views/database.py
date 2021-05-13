from flask import Blueprint, render_template
import models
from database import db_insert, db_delete

app = Blueprint('database', __name__)

# insert
@app.route('/insert/<param>')
def insert(param):
    html_main = "You Can Insert Datum."
    if param == "0":
        html = "Please Input <param>"
    else:
        test_new = models.Test(data=param)
        db_insert(test_new)
        html = "insert: %s" % (param)
    return render_template('sub.html', page_title="Insert", html_main=html_main, html_sub=html)

# update
@app.route('/update/<id>/<param>')
def update(id, param):
    html_main = "You Can Update an Id."
    if id == "0" and param == "0":
        html = "Please Input <id> and <param>"
    else:
        test_up = models.Test.query.filter_by(id=id).first()
        test_up.data=param
        db_insert(test_up)
        html = "update(id:%s): to %s" % (id, param)
    return render_template('sub.html', page_title="Update", html_main=html_main, html_sub=html)

# delete
@app.route('/delete/<id>')
def delete(id):
    html_main = "You Can delete an Id."
    if id == "0":
        html = "Please Input <id>"
    else:
        test_del = models.Test.query.filter_by(id=id).first()
        db_delete(test_del)
        html = "delete: id:%s" % (id)
    return render_template('sub.html', page_title="Delete", html_main=html_main, html_sub=html)
