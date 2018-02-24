from flask import Flask, render_template, request
# from tkinter import messagebox
import json
from difflib import get_close_matches as gcm

data = json.load(open('data.json'))

# global word
# global output

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about_app/')
def about_app():
    return render_template("about_app.html")

@app.route('/about/')
@app.route('/about/', methods=['POST'])
def about():
    word = request.form['search']
    word = word.lower()
    output = ''
    if word in data:
        output = data[word]
    elif word.title() in data:
        output = data[word.title()]
    elif word.upper() in data:
        output = data[word.upper()]
    elif len(gcm(word, data.keys())) > 0:
        # res = messagebox.askquestion("D", "Did you mean %s instead? 'yes' or 'no': " % gcm(word, data.keys())[0], icon='warning')
        # res = input("Did you mean %s instead? 'yes' or 'no': " % gcm(word, data.keys())[0])
        response = " %s " % gcm(word, data.keys())[0]
        output = data[gcm(word, data.keys())[0]]

        if type(output) == list:
            for item in output:
                return render_template("about.html", bot = [response, item])
        else:
            return render_template("about.html", bot = [response, output])


        # return render_template("about.html", bot = [response, output])

        # res = request.form['req']
        # if res == 'yes':
        # else:
        #     output = "The word doesn't exist. Please double check it."
    else:
        output = "The word doesn't exist. Please double check it."
    if output:
        if type(output) == list:
            for item in output:
                return render_template("result.html", bot = item)
        else:
            return render_template("result.html", bot = output)

# @app.route('/about1/')
# @app.route('/about1/', methods=['POST'])
# def about1():
#     word = request.form['search']
#     word = word.lower()
#     output = ''
#     if word in data:
#         output = data[word]
#     elif word.title() in data:
#         output = data[word.title()]
#     elif word.upper() in data:
#         output = data[word.upper()]
#     elif len(gcm(word, data.keys())) > 0:
#         res = messagebox.askquestion("D", "Did you mean %s instead? 'yes' or 'no': " % gcm(word, data.keys())[0], icon='warning')
#         res = input("Did you mean %s instead? 'yes' or 'no': " % gcm(word, data.keys())[0])
#         response = " '%s'? " % gcm(word, data.keys())[0]
#         return render_template("about.html", bot = response)
#
#     res = request.form['req']
#     if res == 'yes':
#         output = data[gcm(word, data.keys())[0]]
#             # else:
#             #     output = "The word doesn't exist. Please double check it."
#     else:
#         output = "The word doesn't exist. Please double check it."
#     if output:
#         if type(output) == list:
#             for item in output:
#                 return render_template("result.html", bot = item)
#         else:
#             return render_template("result.html", bot = output)



if __name__=="__main__":
    app.run(debug=True)
