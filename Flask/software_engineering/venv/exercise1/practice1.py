from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_dongguk():
    return '2016112220 양소영<br>Hello Dongguk University Students!'

if __name__ == '__main__':
    app.run(debug=True)