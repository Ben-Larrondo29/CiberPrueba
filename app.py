from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Prueba 3 BENJAMIN LARRONDO"

if __name__ == '__main__':
    app.run(debug=True)
