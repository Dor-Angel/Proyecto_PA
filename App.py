
from bd import iniciar_bd
app, mysql = iniciar_bd()

from consultas.usuario import consultas_usuario
consultas_usuario(app, mysql)


if __name__ == '__main__':
    app.run(port=3000, debug=True)