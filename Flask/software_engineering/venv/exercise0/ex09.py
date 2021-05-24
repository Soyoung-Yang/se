from flask import Flask
app = Flask(__name__)

def hello_ice():
    return 'Hello ICE students!'
app.add_url_rule('/hello','hello', hello_ice)

if __name__ == '__main__':
    app.run(debug=True)