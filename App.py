from init_app import crear_app

app = crear_app()

if __name__ == '__main__':
    app.run(port=3000, debug=True)