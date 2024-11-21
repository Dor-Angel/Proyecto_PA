from flask import render_template, request, redirect, url_for, flash
from init_app import mysql

def register_routes(app):
    @app.route('/dvds')
    def dvds():
        dvds_data = get_all_dvds()
        return render_template('dvds.html', dvds=dvds_data)

    @app.route('/edit_dvd/<int:id_dvd>', methods=['GET', 'POST'])
    def edit_dvd(id_dvd):
        if request.method == 'POST':
            id_rentor = request.form['id_rentor']
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            fecha_salida = request.form['fecha_salida']
            genero = request.form['genero']
            precio = request.form['precio']
            update_dvd(id_dvd, id_rentor, nombre, descripcion, fecha_salida, genero, precio)
            flash('DVD actualizado correctamente')
            return redirect(url_for('dvds'))
        
        dvds_data = get_all_dvds()
        dvd = next((d for d in dvds_data if d[0] == id_dvd), None)
        return render_template('edit_dvd.html', dvd=dvd)

