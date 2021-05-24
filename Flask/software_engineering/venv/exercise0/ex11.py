from flask import Flask, redirect, url_for
app = Flask(__name__)

# URL에서 인수 값을 받는 함수 hello_user(userName)
@app.route('/user/<userName>') 
def hello_user(userName):
    if userName == 'dongguk': # hell0_user() 함수가 받은 argument가 'dongguk'과 일치하는지 판단
        return redirect(url_for('hello_dongguk')) # url_for의 첫번째 인수: 함수이름  # hello_dongguk으로 redirect
    else:
        return redirect(url_for('hello_student', stdName = userName)) # 함수이름, 두번째 인수: URL의 변수 부분에 해당하는 키워드 인수
        # hello_student 함수로 userName을 담은 stdName 변수를 보내주고 redirect

@app.route('/dongguk')
def hello_dongguk():
    return 'Hello Dongguk University!'

@app.route('/student/<stdName>')
def hello_student(stdName):
    return 'Hello %s!' %stdName

if __name__ == '__main__':
    app.run(debug=True)