from flask import Flask, render_template, request
from flask_mysqldb import MySQL 
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='CentralParkConv',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__,static_url_path='',
            static_folder='',
            template_folder='')


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
          #cursor.execute("insert into grades values('Ron', 3, 4, 5)")
          #cursor.execute("""insert into grades (f_name, hi, user_password, user_email) values (%(_name)s, %(_physics)s, %(_chemistry)s, %(_math)s)""",params)
          #query= "INSERT INTO grades(f_name,sub1,sub2,sub3) VALUES(%s,%s,%s,%s)"
          query= "INSERT INTO survey VALUES(" + "'" + subject1 + "'" + ',' + "'" + subject2 + "'" + ',' + "'" + subject3 + "'" + ',' + "CURDATE()" + ',' + "CURTIME()" +")"
          #query2 = "SELECT * from grades"
          #cursor.execute(query,(first_name,subject1,subject2,subject3))
          cursor.execute(query)
          #cursor.execute(query2)
          connection.commit()
          #nprint()
      finally:
          return "Saved successfully."
  else:
      return "error"
      
if __name__ == '__main__':
   app.run(debug = True)