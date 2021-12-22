from flask import Flask
from flask import request, make_response, redirect, abort
from flask import redirect, render_template, request
app = Flask(__name__)

users = [{'username': 'jpterov', 'name': 'John',
          'surname': 'Petrov', 'age': 19},
         {'username': 'aivanov', 'name': 'Alex',
          'surname': 'Ivanov', 'age': 21}]

@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/users')

@app.route('/user/<name>')
def user(name):
   return '<h1>Hello, %s!</h1>' % name


@app.route('/user/<user_id>/check')
def user_id(user_id):
    for  value in users[0].items():
        if str(value[0]) == user_id:
            return '<h1>Hi, %s!</h1>' %user_id
        else:
            return '<h1>Error, 404!</h1>'


@app.route('/users', methods=['get'])
def all_user():
    #dict_name = dict.values(users)
    return render_template("all_users.html", username = users) #непонятно, как достать значения из словаря, user[username] не работает

if __name__ == '__main__':
    app.run(debug=True)


