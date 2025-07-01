from flask import Flask
import os

app = Flask(__name__)

@app.route("/product")
def get_product():
    return {"product": "Laptop"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
