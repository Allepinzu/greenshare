from flask import Flask, render_template, flash, session, redirect, url_for, request
from form import ContectForm

app = Flask(__name__)
username = ''

app.config['SECRET_KEY'] = 'hard to guess'


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/user', methods=["POST"])
def user():  # put application's code here
    return render_template('user.html')


app.config['SECRET_KEY'] = 'hard to guess'


@app.route('/contact', methods=['GET', 'POST'])
def contact_pages():
    form = ContectForm()
    pagename = "Contact Form"
    name = None
    if form.validate_on_submit():
        name = form.name.data
    return render_template('contact.html', pagename=pagename, form=form, name=name)


@app.route('/login', methods=["POST", "GET"])
def login():  # put application's code here

    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        flash("Login successful", "info")
        return redirect(url_for("user"), user=request.form["nm"])
    else:
        if "user" in session:
            flash("Already logged")
            return redirect(url_for("home"))
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=bool)
