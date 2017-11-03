import datetime
import os
import psycopg2
import sys



from flask import Flask
from flask import render_template


app = Flask(__name__)


dsn_database = "compose"       
dsn_hostname = "sl-us-south-1-portal.6.dblayer.com"     
dsn_port = "26746"                 
dsn_uid = "admin"        
dsn_pwd = "SUKFLLJHQIUQQJLE"      




try:
    conn_string = "host="+dsn_hostname+" port="+dsn_port+" dbname="+dsn_database+" user="+dsn_uid+" password="+dsn_pwd
    print("Connecting to database: " + conn_string)
    conn=psycopg2.connect(conn_string)
    print("Connected!\n")
except:
    print("Unable to connect to the database.")



@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)


