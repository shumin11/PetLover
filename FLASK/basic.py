from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/') #http://127.0.0.1:5000
def index():
    # user_logged_in = False

    # name = "Shumin"
    # letters = list(name)
    # pup_dictionary = {'pup_name':'Sammy'}
    # puppies = ['Fluffy', 'Rufus', 'Spike']

    # return render_template('basic.html', name = name, letters = letters, 
    #                        pup_dictionary = pup_dictionary, puppies = puppies, user_logged_in = user_logged_in)
    return render_template('home.html')

# @app.route('/puppy_name/<name>') #http://127.0.0.1:5000/information
# def puppylatin(name):
    
#     pupname = ''

#     if name[-1] == 'y':
#         pupname = name[:-1] + 'iful'
#     else:
#         pupname = name + 'y'

#     return "<h1> Your puppy latin name is: {}".format(pupname)

@app.route('/puppy/<name>') #http://
def puppy_name(name):
    return render_template('puppy.html', name = name)

if __name__ == '_main_':
    app.run(debug=True)


