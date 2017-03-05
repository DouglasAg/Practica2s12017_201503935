class NodoLista:
	def __init__(self):
		self.valor=""
		self.siguiente=None


	def __str__(self):
		return str(self.carga)

	def getValor(self):
		return self.valor

	def setValor(self,valor):
		self.valor=valor

	def getSiguiente(self):
		return self.siguiente

	def setSiguiente(self,siguiente):
		self.siguiente=siguiente


class Lista:
	def __init__(self):
		self.inicio=None
		self.tamanio=0

	def nueva(self):
		self.inicio=None
		self.tamanio=0

	def esVacio(self):
		return self.inicio==None

	def getTamanio(self):
		return self.tamanio

	def agregarInicio(self,valor):
		nuevo=NodoLista()
		nuevo.setValor(valor)
		if self.esVacio():
			self.inicio=nuevo
		else:
			nuevo.setSiguiente(self.inicio)
			self.inicio=nuevo
		self.tamanio+=1

	def agregarFinal(self,valor):
		nuevo= NodoLista()
		nuevo.setValor(valor)
		if self.esVacio():
			self.inicio=nuevo
		else:
			aux=self.inicio
			while aux.getSiguiente()!=None:
				aux=aux.getSiguiente()
			aux.setSiguiente(nuevo)
		self.tamanio+=1

	def eliminar(self,ind):
		if self.esVacio():
			return "Lista Vacia"
		else:
			if ind==0:
				self.inicio=self.inicio.getSiguiente()
				return "Elemento elimindad"
			else:
				cont=1
				aux = self.inicio
				aux2 = self.inicio
				while aux.getSiguiente() != None:
					aux = aux.getSiguiente()
					if ind == cont:
						break
					aux2=aux2.getSiguiente()
					cont+= 1
				aux2.setSiguiente(aux.getSiguiente())
				return "Elemento eliminado en indice " + str(cont)


	def listar(self):
		if self.esVacio()!=True:
			aux=self.inicio
			i=0
			mostrar=""
			while aux!=None:
				mostrar = mostrar + str(aux.getValor()) + " ---> "

				aux=aux.getSiguiente()
				i+=1
		return mostrar

	def buscar(self,ref):
		aux=self.inicio
		encontrado=False
		cont=0
		while aux!=None and encontrado!= True:
			if ref==aux.getValor():
				encontrado=True
			else:
				aux=aux.getSiguiente()
				cont+=1
		if encontrado==True:
			return "Encontrado en el indice: " + str(cont)
		else:
			return "No se encontro el dato"

	def getInicio(self):
		return self.inicio


