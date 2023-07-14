from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') #http://127.0.0.1:5000
def index():
    return render_template('basic.html')


@app.route('/puppy_name/<name>') #http://127.0.0.1:5000/information
def puppylatin(name):
    
    pupname = ''

    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'

    return "<h1> Your puppy latin name is: {}".format(pupname)


if __name__ == '_main_':
    app.run(debug=True)


