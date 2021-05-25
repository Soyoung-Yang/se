from flask import Flask
app = Flask(__name__)

@app.route('/hello/<nm>') # url 입력할 때 <nm> 위치에 이름 쓰기(<nm>: 변수)
def hello_ice(nm):
    return 'Hello ICE student %s!' %nm

if __name__ == '__main__':
    app.run(debug=True)