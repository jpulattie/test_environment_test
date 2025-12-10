from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    words = "Hello World 4"
    return render_template("index.html", words=words)


if __name__ == '__main__':
    app.run(debug=True)

