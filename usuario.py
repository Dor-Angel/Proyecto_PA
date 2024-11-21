from flask import render_template, request, redirect, url_for, flash
from init_app import mysql

def register_routes(app):
    @app.route('/')
    def Index():
        cur= mysql.connection.cursor()
        cur.execute('select * from usuario')
        data=cur.fetchall()
        cur.close()
        return render_template('usuario.html',contacts=data)
    @app.route('/add_usuario', methods=['POST'])
    def add_usuario():
        if request.method=='POST':
            nombre =request.form['nombre']
            apellido =request.form['apellido']
            email =request.form['email']
            contraseña =request.form['contraseña']
            fecha_nac =request.form['fecha_nac']
            descripcion =request.form['descripcion']
            cur= mysql.connection.cursor()
            cur.execute('INSERT INTO usuario (fullname,phone,email) VALUES (%s, %s ,%s)',(nombre,apellido,email,contraseña,fecha_nac,descripcion))
            mysql.connection.commit()
            cur.close()
            flash('usuario agregado satisfactoriamente')
            return redirect(url_for('Index'))
    @app.route('/edit/<id>')
    def get_usuario(id):
        cur=mysql.connection.cursor()
        cur.execute('select * from usuario where id={0}'.format(id)  )
        data=cur.fetchall()
        print(data[0])
        return render_template('edit-contact.html',contact=data[0])
    @app.route('/update/<id>', methods=['POST'] )
    def update_usuario(id):
        if request.method=='POST':
            nombre =request.form['nombre']
            apellido =request.form['apellido']
            email =request.form['email']
            contraseña =request.form['contraseña']
            fecha_nac =request.form['fecha_nac']
            descripcion =request.form['descripcion']
            cur=mysql.connection.cursor()
            cur.execute('update usuario set fullname=%s, phone=%s, email=%s where id={0}'.format(id), (nombre,apellido,email,contraseña,fecha_nac,descripcion)) 
            mysql.connection.commit()
            print(id)
            cur.close()
            flash('datos actualizados satisfactoriamente')
            return redirect(url_for('Index'))
    @app.route('/delete/<string:id>')
    def delete_usuario(id):
        cur=mysql.connection.cursor()
        cur.execute('delete from usuario where id={0}'.format(id))
        mysql.connection.commit()
        cur.close()
        flash('datos eliminados satisfactoriamente')
        return redirect(url_for('Index'))