from flask import Flask, render_template
# render_template() 함수로 HTML 파일을 rendering 할 수 있다.
# Flask는 이 python 스크립트가 있는 동일한 폴더(exercise0)의 templates 폴더에서 HTML 파일을 찾으려고 한다.
app = Flask(__name__)

@app.route('/')
def hello_class():
    return render_template('class.html')

if __name__ == '__main__':
    app.run(debug=True)