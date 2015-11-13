from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms.validators import Email



app=Flask(__name__)
app.config['SECRET_KEY']='I guess you can see'

moment=Moment(app)
manager = Manager(app)
bootstrap=Bootstrap(app)
class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')

@app.route('/',methods=["GET","POST"])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template('index.html',name=name, form=form, current_time = datetime.utcnow())
#current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
        
@app.errorhandler(500)
def internal_server_error(e):
   return render_template('500.html'),500

if __name__=='__main__':
    manager.run()

