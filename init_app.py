from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()

def crear_app():
    app=Flask(__name__)
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']=''
    app.config['MYSQL_DB']='rentas_dvds'
    app.secret_key ='mysecretkey'
    mysql.init_app(app)
    from consultas import registrar_consultas
    registrar_consultas(app)
    return app