from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "這是我的佈署，第五次!!"


if __name__=="__main__":
    app.run(host='0.0.0.0',port=3000,debug=True)