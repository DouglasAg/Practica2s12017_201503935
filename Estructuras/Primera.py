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
	return str(mostrar)

@app.route('/nuevaCola')
def nueva():
	Col.nueva()
	return "Cola nueva"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')