from flask import Flask, render_template, request

app = Flask(__name__,
            static_url_path='',
            static_folder='',
            template_folder='templates')

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("index.html",result = result)

if __name__ == '__main__':
    app.run(debug = True)