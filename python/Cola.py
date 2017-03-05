class NodoCola:
	def __init__(self):
		self.valor=0
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

class Cola:
	def __init__(self):
		self.inicio=None
		self.tamanio=0

	def esVacio(self):
		return self.inicio==None

	def getTamanio(self):
		return self.tamanio

	def agregar(self,valor):
		nuevo= NodoCola()
		nuevo.setValor(valor)

		if self.esVacio():
			self.inicio=nuevo
		else:
			aux=self.inicio
			while aux.getSiguiente()!=None:
				aux=aux.getSiguiente()
			aux.setSiguiente(nuevo)
		self.tamanio+=1

	def eliminar(self):
		aux=NodoCola()
		aux=self.inicio
		if aux.getSiguiente()==None:
			self.inicio=None
		else:
			self.inicio=aux.getSiguiente()
		self.tamanio-=1
		return aux.getValor()

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

	def getInicio(self):
		return self.inicio
