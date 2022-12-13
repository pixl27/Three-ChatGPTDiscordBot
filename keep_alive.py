from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return 'Keep the server alive page'

def run():
    app.run('0.0.0.0',port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()