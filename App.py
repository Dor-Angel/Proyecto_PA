from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskcontact'
app.secret_key ='mysecretkey'
mysql.init_app(app)
from consultas.consulta import registrar_consultas
registrar_consultas(app, mysql)

if __name__ == '__main__':
    app.run(port=3000, debug=True)