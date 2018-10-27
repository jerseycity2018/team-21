from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='cpc',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__,
            static_url_path='',
            static_folder='../frontend',
            template_folder='../frontend')


@app.route('/',methods=['GET','POST'])
def get_data():
    if request.method == 'GET':
        print("serving.survey.html")
        return render_template("survey.html")
    if request.method == 'POST':

        subject1 = request.form['Age']
        subject2 = request.form['Tourist']
        subject3 = request.form['Activity']

        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO survey VALUES('"+subject1+"','"+subject2"','"+subject3+"','"+CURDATE()+"','"+CURTIME()+")"
                cursor.execute(query)
                connection.commit()
        finally:
            return "Saved successfully."
    else:
        return "error"
      
if __name__ == '__main__':
   app.run(debug = True)
