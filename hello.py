from flask import Flask, request
# from flask.ext.script import Manager
app = Flask(__name__)
# manager = Manager(app)
@app.route('/user/<name>')
def index(name):
    return '<h1> Hello, %s</h1>' % name

if __name__ == '__main__':

    app.run(debug=True)