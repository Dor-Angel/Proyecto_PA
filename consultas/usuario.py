from flask import render_template, request, redirect, url_for, flash

def consultas_usuario(app, mysql):
    @app.route('/')
    def Index():
        cur= mysql.connection.cursor()
        cur.execute('select * from usuario')
        data=cur.fetchall()
        cur.close()
        return render_template('index.html', usuarios=data)
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
            cur.execute('INSERT INTO usuario (nombre, apellido, contraseña, email, fecha_nac, descripcion) VALUES (%s, %s ,%s, %s ,%s ,%s)',(nombre,apellido,email,contraseña,fecha_nac,descripcion))
            mysql.connection.commit()
            cur.close()
            flash('usuario agregado satisfactoriamente')
            return render_template('rentor.html')
    @app.route('/edit/<id>')
    def get_usuario(id):
        cur=mysql.connection.cursor()
        cur.execute('select * from usuario where id_usuario={0}'.format(id)  )
        data=cur.fetchall()
        print(data[0])
        return render_template('edit_usuario.html',contact=data[0])
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
            cur.execute('update usuario set nombre=%s, apellido=%s, email=%s, contraseña=%s, fecha_nac=%s, descripcion=%s where id_usuario={0}'.format(id), (nombre,apellido,email,contraseña,fecha_nac,descripcion)) 
            mysql.connection.commit()
            print(id)
            cur.close()
            flash('datos actualizados satisfactoriamente')
            return redirect(url_for('Index'))
    @app.route('/delete/<string:id>')
    def delete_usuario(id):
        cur=mysql.connection.cursor()
        cur.execute('delete from dvd where id_rentor={0}'.format(id))
        cur.execute('delete from rentor where id_usuario={0}'.format(id))
        
        cur.execute('delete from usuario where id_usuario={0}'.format(id))
        
        mysql.connection.commit()
        cur.close()
        flash('datos eliminados satisfactoriamente')
        return redirect(url_for('Index'))