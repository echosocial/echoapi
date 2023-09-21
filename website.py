from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "this doesnt work rn so i dont know what to do lmao"
