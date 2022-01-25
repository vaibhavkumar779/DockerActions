from flask import Flask,render_template
p1 = Flask(__name__)

@p1.route('/')
def assigment():
    return render_template('try.html')
