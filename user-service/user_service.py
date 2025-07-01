from flask import Flask
app = Flask(__name__)

@app.route("/user")
def get_user():
    return {"user": "John Doe"}

if __name__ == "__main__":
    app.run(port=5001)
