from flask import Flask
app = Flask(__name__)

@app.route('/hello/<int:stdID>')
def hello_ice(stdID):
    return '2016112220 양소영<br>Hello ICE student %d!' %stdID

@app.route('/flt/<float:float>')
def floatNum(float):
    return '2016112220 양소영<br>The number is %f!' %float

if __name__ == '__main__':
    app.run(debug=True)