from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    # 0.0.0.0 makes the app reachable outside this process/container.
    app.run(host="0.0.0.0", port=5000, debug=False)
