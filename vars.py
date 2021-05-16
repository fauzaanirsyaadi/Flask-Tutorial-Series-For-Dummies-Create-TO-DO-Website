from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
  # return 'Hi'
  return render_template('hello.html', list_of_name=['fauzaan', 'irsyaadi'])

@app.route('/<string:name>')
def greet(name):
  return f'Hello {name}'

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
