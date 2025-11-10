import os
from flask import Flask, render_template, request, redirect, url_for,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Flask App!"

@app.route('/index', methods=['GET'])
def index():
    return "This is the index page."

@app.route('/success/<score>')
def success(score):
   return "The person is passed with score: " + score

@app.route('/failure/<score>')
def failure(score):
   return "The person is failed with score: " + score

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        math = float(request.form['math'])
        physics = float(request.form['physics'])
        chemistry = float(request.form['chemistry'])
        total = math + physics + chemistry
        average = total / 3

        if average >= 50:
            res = "success"
        else:
            res = "failure"

        return redirect(url_for(res, score=average))
    

@app.route('/api', methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val + b_val)

if __name__ == "__main__":
    app.run(debug=True)
