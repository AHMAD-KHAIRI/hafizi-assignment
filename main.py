import os
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")

@app.route("/")
def home():
    return render_template("a_index.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=False)