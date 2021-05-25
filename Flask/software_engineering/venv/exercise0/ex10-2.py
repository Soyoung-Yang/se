from flask import Flask
app = Flask(__name__)

@app.route('/hello/<stdName>')
def hello_studentName(stdName):
    return 'Hello student %s' %stdName

@app.route('/hello/<int:stdID>')
def hello_studentID(stdID):
    return 'The student ID is %d' %stdID

@app.route('/hello/<float:flt>')
def floatNum(flt):
    return 'The number is %f' %flt

if __name__ == '__main__':
    app.run(debug=True)