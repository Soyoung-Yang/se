from flask import Flask, request, render_template, session, url_for, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
userinfo = {'Soy': 'seproject^3^'}
board = []
 
@app.route("/")
def home():
    if session.get('logged_in'):
        return render_template('list.html')
    else:
        return render_template('index.html')
 
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        try:
            if (userid in userinfo):
                session["logged_in"] = True
                return render_template('list.html')
            else:
                return 'Wrong Password'
            return 'Cannot find ID'
        except:
            return 'Dont login'
    else:
        return render_template('login.html')
 
 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form['userid'] 
        password = request.form['password']
        userinfo[userid] = password
        
        return redirect(url_for('login'))
    else:
        return render_template('register.html')
 
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')


# List diaries (Read)
@app.route('/diary')
def index2():
    return render_template('list.html', rows=board)
 
# Upload Diaries (Create)
@app.route('/add',methods=["POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        context = request.form["context"]
        board.append([name,context])
        return redirect(url_for("index2"))
    else:
        return render_template("list.html", rows=board)
 
# Update Diaries
@app.route('/update/<int:uid>', methods=["GET","POST"])
def update(uid):
    if request.method == "POST":
        index2 = uid - 1
        name = request.form["name"]
        context = request.form["context"]
        
        board[index2] = [name,context]   # ????????? board????????? ????????????
        return redirect(url_for("index2"))
    else:
        return render_template("update.html",index2=uid,rows=board)
 
# Delete Diaries
@app.route('/delete/<int:uid>')
def delete(uid):
    index2 = uid - 1
    del board[index2]
    return redirect(url_for("index2"))

# file upload
@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.exists("./static"):
            os.makedirs('./static')
        f.save('./static/' + secure_filename(f.filename))
        return redirect(url_for("index2"))
    else:
        return render_template("list.html", rows=board)

if __name__ == '__main__':
    app.run(debug=True)
