from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return"Hellou"

@app.route("/about")
def about():
    return"<h1>Hellou About</h1>"

if __name__== "__main__":
    app.run(debug=True, port=5010)