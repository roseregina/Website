from main import app
from flask import render_template, request, redirect, url_for
from flaskext.login import current_user
from flaskext.wtf import Form, TextField, Email, Required, IntegerField
from users import NextURLField

class VolunteerLogin(Form):
    email = TextField('Email', [Email(), Required()])
    phone_number = IntegerField('Number', [Required()])
    next = NextURLField('Next')
    
@app.route("/volunteer_login", methods=['GET', 'POST'])
def volunteer_login():
    if not current_user.is_authenticated():
        return redirect(request.args.get('next', url_for('login')))
    form = VolunteerLogin(request.form, next=request.args.get('next'))
    # if request.method == 'POST' and form.validate():
        # user = User.query.filter_by(email=form.email.data).first()
        # if user and user.check_password(form.password.data):
        #     login_user(user)
        #     return redirect(form.next.data or url_for('tickets'))
        # else:
        #     flash("Invalid login details!")
    return render_template('volunteer-login.html', form=form)