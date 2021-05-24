from flask import Flask, render_template
app = Flask(__name__)

@app.route('/results')
def show_result():
    dict = {'Soyoung':100, 'Jingu':90, 'Ahyun':80}
    return render_template('results.html', result = dict)

if __name__ == '__main__':
    app.run(debug=True)