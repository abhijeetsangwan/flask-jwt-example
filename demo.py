'''
Created on Oct 3, 2016

@author: abhijeetsangwan
'''


from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required
import sqlite3 as lite
import datetime


class User(object):
    def __init__(self, id_, username, password):
        self.id = id_
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


def authenticate(username, password):
    con = lite.connect('login.db')
    cur = con.cursor()
    sql = 'select id from login where user=? and pass=?'
    cur.execute(sql, (username, password,))
    data = cur.fetchone()
    if data is not None:
        return User(data[0], username, password)
    else:
        return None


def fetch_user(user_id):
    con = lite.connect('login.db')
    cur = con.cursor()
    sql = 'select user, pass from login where id=?'
    cur.execute(sql, (user_id,))
    data = cur.fetchone()
    if data is not None:
        return User(user_id, data[0], data[1])
    else:
        return None


def identity(payload):
    print ('identity payload', payload)
    user_id = payload['identity']
    print ('user id is', user_id, 'type', type(user_id))
    return fetch_user(user_id)


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_URL_RULE'] = '/authorize-me'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)
jwt = JWT(app, authenticate, identity)



@app.route('/protected', methods=['POST'])
@jwt_required()
def protected():
    return jsonify({'data': 'something'})


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=10001)
