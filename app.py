from flask import Flask, render_template
import math
app = Flask(__name__)

#                EJEMPLO
# @app.route('<ruta virtual de la web>')
# def inicio():
#     return render_template("<html a renderizar para darselo al usuario>")

# La pagina principal
@app.route('/')
def inicio():
    return render_template("index.html")

# Pagina potencia
@app.route('/potencia/<int:base>/<int:exponente>',methods=["GET","POST"])
def saluda(base,exponente):
	if exponente >= 1:
		resultado=base*exponente
	if exponente == 0:
		resultado=1
	if exponente < 0:
		resultado=1/base * math.abs(exponente)
	return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)




app.run(
	"0.0.0.0", # Direccion ip, si es 0.0.0.0 es cualquier ip, si es 127,0,0,1 solo puede entrar desde el mismo equipo.
	8000, # Puerto de la web
	debug=True #Es para depurar la página, que si tenemos algun error se nos muestra en el navegador web.
        ) # Ejecuta el servidor web
