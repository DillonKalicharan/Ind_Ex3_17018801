from flask import Flask, render_template, flash, redirect,url_for
from forms import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '0123456789'

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'It worked :D')
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
