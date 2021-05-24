from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/hello/<stdName>')
def hello(stdName):
    return 'Welcome %s!' %stdName
# login.html의 http://localhost:5000/login 은 login 함수로 mapping 됨
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        student = request.form['nm'] # form data에서 얻은 'nm' 매개변수 값을 student에 저장
        return redirect(url_for('hello', stdName = student)) # 변수 student는 '/hello' URL에 전달된다.
    else:
        student = request.args.get('nm') #args: form 매개변수 쌍과 해당 값의 목록을 포함하는 dictionary object
        return redirect(url_for('hello', stdName = student)) # 'nm' 매개변수에 해당하는 값은 '/hello' URL로 전달된다.

if __name__ == '__main__':
    app.run(debug=True)


''' 
<Form> 태그 : client에서 server로 데이터 전송하기 위한 방법😊
1. 기본구조
    - method 속성과 action 속성을 가짐
    - method 속성 : 데이터를 넘겨주는 방식 설정, post와 get 방식
    - action 속성 : 클라이언트로부터 전송된 데이터들을 처리할 ASP 문서 지정
    <form method="post" action="process.asp">
    (데이터 입력 양식들)
    </form>
2. 글 입력 상자(text input box)
    - name  속성 : 클라이언트 -> 서버 로 전송되었을 때, 서버측에서 사용할 변수 이름에 해당
3. Request와 Response 객체
    - 웹서비스는 HTTP 서비스 프로토콜을 통해 클라이언트와 서버가 통신을 한다.
    - 웹 서버는 클라이언트가 http를 통해 전송해온 요청을 받아 Request에 저장한다.
    - <form>..</form>을 통해 클라이언트에서 서버로 넘겨진 데이터는 request 객체 내에 저장이 되고, 서버는 request객체를 검색하여 해당 데이터 처리를 한다.
4. Request 객체
    - Form : 클라이언트가 전송한 Form 요소 값
5. HTTP 통신의 메시지 형식
    - 클라이언트에서 서버로 데이터 보낼 때, <form> 태그를 이용해 보냄
    - 이때, method="post"일 때와 method="get"일 때 통신 방법이 다름
    - method="get" : 입력 데이터들이 URL 뒤에 QueryString으로 추가되어 전송됨
    - method="post" : 입력 데이터들이 HTTP 메시지의 데이터 부분에 첨부되어 전송됨 


출처 : https://m.blog.naver.com/PostView.nhn?blogId=starcast&logNo=60007341828&proxyReferer=https:%2F%2Fwww.google.com%2F
'''