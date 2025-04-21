from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! A aplicação Flask está rodando no Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
