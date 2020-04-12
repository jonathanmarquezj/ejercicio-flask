from flask import Flask, render_template
app = Flask(__name__)

#                EJEMPLO
# @app.route('<ruta virtual de la web>')
# def inicio():
#     return render_template("<html a renderizar para darselo al usuario>")

@app.route('/')
def inicio():
    return render_template("index.html")

app.run(
	"0.0.0.0", # Direccion ip, si es 0.0.0.0 es cualquier ip, si es 127,0,0,1 solo puede entrar desde el mismo equipo.
	8000, # Puerto de la web
	debug=True #Es para depurar la página, que si tenemos algun error se nos muestra en el navegador web.
        ) # Ejecuta el servidor web
