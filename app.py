from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>UPI Fraud Detection</h1>
    <p>Welcome to the UPI Fraud Detection Project.</p>
    <p>Project created using Python and Flask.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
