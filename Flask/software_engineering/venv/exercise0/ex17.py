from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

app.secret_key = 'software_engineering'

# URL '/'는 세션변수 'username'이 설정되지 않았으므로 사용자에게 로그인하라는 메시지를 표시한다.
@app.route('/')
def index():
    # session 변수가 결정되고 redirect 된 후 session 변수 'username'이 발견된다.
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
            "<b><a href = '/logout'>Click here to log out</a></b>"
    return "You are not logged in <br><b><a href = '/login'>" + \
        "Click here to log in</b></a>"

# 사용자가 '/login'으로 들어오면서 login() view 함수는 POST 메소드를 통해 호출되고, 로그인 양식을 열게 된다.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
        # 양식이 '/login'에 다시 게시되고 이제 session 변수가 결정된다.
        # 애플리케이션이 '/'로 redirect 된다. 이번에는 session 변수 'username'이 발견된다.
    return '''
    <form action = "" method = "POST">
        <p><input type = text name = username /></p>
        <p><input type = submit value= login /></p>
    </form>
    '''

# 애플리케이션에는 'username' session 변수를 표시하는 logout() view 함수도 포함되어 있다. 따라서 '/' URL은 다시 첫 페이지를 표시하게 된다.
@app.route('/logout')
def logout():  
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)