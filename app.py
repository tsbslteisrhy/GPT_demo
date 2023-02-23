from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(host='0.0.0.0', port="8080", debug=True)