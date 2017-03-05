from flask import Flask, request
from Estructuras import Cola
from Estructuras import ListaSimple
from Estructuras import Pila

app=Flask("Practica_2")

Col=Cola.Cola()
Pil=Pila.Pila()
Lis=ListaSimple.Lista()

@app.route('/Conectar')
def conectar():
	return "Si conecto"

@app.route("/AgregarCola", methods=['POST'])
def agregarcol():
	num=str(request.form['dato'])
	Col.agregar(num)
	return "Dato Ingresado: " + str(num)

@app.route('/listarCola')
def listarcol():
	mostrar=Col.listar()
	return str(mostrar)

@app.route('/eliminarcol')
def elimcol():
	mostrar=Col.eliminar()
	return "Dato eliminado: " + str(mostrar)

@app.route('/nuevaCola')
def nueva():
	Col.nueva()
	return "Cola nueva"

@app.route('/AgregarPila',methods=['POST'])
def agregarpila():
	num=str(request.form['dato'])
	Pil.push(num)
	return "Dato Ingresado: "+ str(num)

@app.route("/listarPila")
def listatpila():
	mostrar=Pil.listar()
	return mostrar

@app.route("/eliminarpila")
def elimpil():
	mostrar=Pil.pop()
	return "Dato eliminado: " + str(mostrar)  

@app.route("/nuevapila")
def nuevapila():
	Pil.nueva()
	return "Pila nueva"

@app.route("/AgregarLista", methods=['POST'])
def Agregarlis():
	num=str(request.form['dato'])
	Lis.agregarFinal(num)
	return "Dato agregado: " + str(num)

@app.route("/listarLis")
def listarlis():
	mostrar=Lis.listar()
	return mostrar

@app.route("/eliminarLis", methods=['POST'])
def eliminarlis():
	num=str(request.form['dato'])
	mostrar=Lis.eliminar(num)
	return "Dato eliminano: " + str(mostrar)

@app.route("/buscarLista", methods=['POST'])
def buscarlis():
	tx=str(request.form['dato'])
	encontro=Lis.buscar(tx)
	return str(encontro)

@app.route("/nuevalista")
def nuevalista():
	Lis.nueva()
	return "Lista nueva"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')