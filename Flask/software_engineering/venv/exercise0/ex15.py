from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        score = request.form
        '''request 객체 : <form>에 의해 서버로 넘어온 데이터를 저장하고, 
        이 중 method='post' 방식으로 넘어온 데이터를 request.form 컬렉션에 저장함 '''
        return render_template("result.html", scores = score)
# result() 함수는 사전 객체의 request.form에 있는 form 데이터를 수집하여 rendering 하기 위해 result.html로 보낸다.

if __name__ == '__main__':
    app.run(debug=True)


# immutable : 값이 변하지 않는