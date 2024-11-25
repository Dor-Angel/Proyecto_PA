from flask import render_template, request, redirect, url_for, flash
from init_app import mysql
def register_routes(app):
    @app.route('/rentas')
    def rentas():
        rentas_data = get_all_rentas()
        return render_template('rentas.html', rentas=rentas_data)

    @app.route('/edit_renta/<int:id_renta>', methods=['GET', 'POST'])
    def edit_renta(id_renta):
        if request.method == 'POST':
            id_rentor = request.form['id_rentor']
            id_dvd = request.form['id_dvd']
            id_usuario = request.form['id_usuario']
            fecha_renta = request.form['fecha_renta']
            fecha_entrega = request.form['fecha_entrega']
            cantidad = request.form['cantidad']
            total = request.form['total']
            update_renta(id_renta, id_rentor, id_dvd, id_usuario, fecha_renta, fecha_entrega, cantidad, total)
            flash('Renta actualizada correctamente')
            return redirect(url_for('rentas'))
        
        rentas_data = get_all_rentas()
        renta = next((r for r in rentas_data if r[0] == id_renta), None)
        return render_template('edit_renta.html', renta=renta)

