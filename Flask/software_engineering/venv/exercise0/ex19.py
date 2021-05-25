from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)

'''
--upload.html
파일을 선택한 후 submit을 클릭한다. 양식의 POST 메소드는 '/uploader' URL을 호출한다. 
--python script
함수 upload_file()는 저장 작업을 수행한다.
'''