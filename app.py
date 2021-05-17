from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  request_method = request.method
  if request.method=="POST":
    print("=====")
    print(request.form)
    print("=====")
    first_name=request.form('first_name')
    return redirect(url_for('name', first_name=first_name))
  return render_template('hello.html', request_method=request_method)

@app.route('/name/<string:first_name>')
def name(first_name):
  return f'{first_name}'
if __name__ == '__main__':#ketika file ini dibuka kita akan langsung ran app.py
  app.run(debug=True)
