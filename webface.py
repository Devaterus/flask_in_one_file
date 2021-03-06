#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (Flask, render_template, Markup, request,
                   redirect, session)
app = Flask(__name__)
############################################################################


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/super/')
def super():
    text = "Dnes je máme programování, což mi udělalo velikou radost :-)"
    return render_template('super.html', text=text)


@app.route('/number/<i>')
def number(i):
    return render_template('number.html', number=i)


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8765, debug=True)
