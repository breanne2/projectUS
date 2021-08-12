from flask import Flask
from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask import Flask,request

mysql = MySQL()
application = Flask(__name__)

@application.route("/index")
def index():
    application.config['MYSQL_HOST'] = 'customerdataus.c9emuq5rjjks.us-east-1.rds.amazonaws.com'
    application.config['MYSQL_PORT'] = '3306'
    application.config['MYSQL_DB'] = 'UScustomerdatadb'
    application.config['MYSQL_USER'] = 'admin'
    application.config['RMYSQL_PASSWORD'] = 'Hollywarner10'

    mysql.init_app(application)

    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * FROM EU_cust_data')
    data = cursor.fetchall()
    return render_template('index.html', output_data=data)

@application.route("/Authenticate")
def Authenticate():

    #app.config['MYSQL_DATABASE_USER'] = 'root'
    #app.config['MYSQL_DATABASE_PASSWORD'] = 'Hollywarner10'
    #app.config['MYSQL_DATABASE_DB'] = 'inventorydb'
    #app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    application.config['RDS_HOSTNAME'] = 'globaldb-us-east.cluster-ro-c9emuq5rjjks.us-east-1.rds.amazonaws.com'
    application.config['RDS_PORT'] = '3306'
    application.config['RDS_DB_NAME'] = 'inventorydb'
    application.config['RDS_USERNAME'] = 'admin'
    application.config['RDS_PASSWORD'] = 'Hollywarner10'

    mysql.init_app(application)

    cursor = mysql.connect().cursor()
    #Productname = request.args.get('productname')
    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * FROM items')
    data = cursor.fetchall()
    if data is None:
        return "Username or Password is wrong"
    else:
        return render_template('inventory.html', output_data=data)

@application.route('/')
def hello_world():
    #return 'London page!'
    return render_template('button.html')

if __name__ == '__main__':
    application.run()
