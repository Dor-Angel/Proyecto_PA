from flask import render_template, request, redirect, url_for, flash
from init_app import mysql

def register_routes(app):
    @app.route('/rentors')
    def rentors():
        rentors_data = get_all_rentors()
        return render_template('rentors.html', rentors=rentors_data)

    @app.route('/edit_rentor/<int:id_rentor>', methods=['GET', 'POST'])
    def edit_rentor(id_rentor):
        if request.method == 'POST':
            id_usuario = request.form['id_usuario']
            clasificacion = request.form['clasificacion']
            update_rentor(id_rentor, id_usuario, clasificacion)
            flash('Rentor actualizado correctamente')
            return redirect(url_for('rentors'))
        
        rentors_data = get_all_rentors()
        rentor = next((r for r in rentors_data if r[0] == id_rentor), None)
        return render_template('edit_rentor.html', rentor=rentor)
