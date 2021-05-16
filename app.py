from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return'<h1>Hello world</h1>'

if __name__ == '__main__':#ketika file ini dibuka kita akan langsung ran app.py
  app.run(debug=True)
