from flask import Flask, render_template, request

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='Students',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__,
            static_url_path='',
            static_folder='../frontend',
            template_folder='../frontend')

@app.route('/survey', methods=['GET','POST'])
def survey():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        form = request.form

        try:
            with connection.cursor() as cursor:
                query = 
                "INSERT INTO Surveys()"
        finally:
    else:
        return "error"

@app.route('/survey', methods=['POST'])
def submit():
    result = request.form
    location = request.args.get('location', default='NULL', type=str)
    
    return render_template("index.html",result = result)

if __name__ == '__main__':
    app.run(debug = True)