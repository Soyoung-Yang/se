# redirect() : 로그인 시도가 실패할 때 로그인 페이지를 다시 표시
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login2.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['ProfName'] == 'Soyoung':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'You have logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)