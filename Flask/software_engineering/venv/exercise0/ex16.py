from flask import Flask, request, render_template, make_response
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

# <cookies 저장> - make_response
@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['username'] # form data에서 얻은 'username' 매개변수 값을 user에 저장
        # request object는 쿠키의 속성이 포함된다. - client가 전송한 모든 쿠키 변수, 해당 값의 dictionary object
        # 그 외에도 쿠키는 사이트의 만료 시간, 경로 및 도메인 이름 저장한다.
    resp = make_response(render_template('readcookie.html')) 
    # make_response() 함수를 사용해서 view 함수의 반환 값에서 response object를 가져온다.
    # 그후 response object의 set_cookie() 함수를 사용하여 쿠키를 저장한다.
    resp.set_cookie('userName', user) # user에 저장된 값을 'userName'에 저장
    return resp

# <cookies 읽기> - request
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userName') # userName : key
    return '<h1>Welcome ' + name + '!</h1>'


if __name__ == '__main__':
    app.run(debug=True)

'''
<쿠키>
쿠키에 접근하기 위해서는 cookies 속성을 사용할 수 있다. 쿠키를 저장하기 위해서는 response 객체의 set_cookie 메소드를 사용할 수 있다. 
request 객체의 cookies 속성은 클라이언트가 전송하는 모든 쿠키를 가지고 있는 dictionary이다. 
만약 여러분이 세션을 사용하기를 원한다면 쿠키를 직접 사용하는 대신에 쿠키 위에서 보안성을 추가한 Flask의 세션 을 사용하라.
쿠키가 response 객체에 저장되는 것을 주목하라. 
여러분이 보통 뷰 함수로부터 단지 문자열을 반환하기 때문에, Flask는 그 문자열들을 여러분을 위해 response 객체로 변환할 것이다. 
만약 여러분이 명시적으로 변환하기를 원한다면 여러분은 make_response() 함수를 사용하여 값을 변경할 수 있다.

출처
https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html
'''