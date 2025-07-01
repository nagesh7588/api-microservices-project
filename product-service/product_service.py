from flask import Flask
app = Flask(__name__)

@app.route("/product")
def get_product():
    return {"product": "Laptop"}
    
if __name__ == "__main__":
    app.run(port=5002)
