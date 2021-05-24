from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_class():
    return '<html><body><h1>Welcome to Software Engineering</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)

# python 코드에서 html 콘텐츠를 생성하는 것은 굉장히 번거롭다.
# Flask의 기반이 되는 jinja2는 템플릿 엔진을 활용할 수 있다.
# render_template() 함수로 html 파일을 rendering 할 수 있다.