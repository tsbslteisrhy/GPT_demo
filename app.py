import os  #절대경로를 지정하기 위한 OS 모듈 import
from flask import Flask
from flask import request  #회원정보를 제출했을 때 받아오기 위한 request, post 요청을 활성화시키기 위함
from flask import redirect  #페이지 이동시키는 함수
from flask import  render_template
from flask import jsonify  #json 데이터를 내보내는 함수
from models import db
from models import Users  #모델의 클래스 가져오기
from flask import session
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm


app = Flask(__name__, static_url_path='/static')
app.config["JSON_AS_ASCII"] = False

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['email'] = form.data.get('email')

        return render_template('list.html', form=form)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        users = Users()
        users.email = form.data.get('email')
        users.password = form.data.get('password')
        users.apikey = form.data.get('apikey')

        #print(users.email, users.password)

        db.session.add(users)
        db.session.commit()

        return render_template('login.html', form=form)
    return render_template('register.html', form=form)

@app.route('/', methods = ['POST'])
def registerDone():
    if request.method == 'POST':
        return render_template('login.html')

# @app.route('/list')
# def list():
#     return render_template('list3.html')

# @app.route('/list')
# def login():
#     email = request.args.get('email')
#     pwd = request.args.get('password')
#     data = {"email":email, "password": pwd}
#     return jsonify(data)

@app.route('/list', methods = ['POST', 'GET'])
def list():
    # email = request.args.get('email')
    # pwd = request.args.get('password')
    # data = {"email":email, "password": pwd}
    if request.method == 'POST':
        return render_template("list.html")
    else:
        email = request.form['email']
        return "Your email is %s" % email

@app.route('/prompt')
def prompt():
    return render_template('prompt.html')

@app.route('/prompt-concept-generate')
def promptConceptGenerate():
    return render_template('prompt-concept-generate.html')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))  # db파일을 절대경로로 생성
    dbfile = os.path.join(basedir, 'db.sqlite')  # db파일을 절대경로로 생성

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'ejwhsqlwmdhs'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port="8080", debug=True)