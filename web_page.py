from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World! </h1> <br> <h2>This is Raspberry Pi Workshop</h2>"

@app.route("/test")
def test():
    return render_template('main.html')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
