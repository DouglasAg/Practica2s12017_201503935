class NodoPila:

	def __init__(self):
		self.valor=0
		self.siguiente=None

	def getValor(self):
		return self.valor

	def setValor(self,valor):
		self.valor=valor

	def getSiguiente(self):
		return self.siguiente

	def setSiguiente(self,siguiente):
		self.siguiente=siguiente

class Pila:
	def __init__(self):
		self.raiz=None

	def esVacia(self):
		return self.raiz==None

	def nueva(self):
		self.raiz=None

	def push(self,valor):
		nuevo=NodoPila()
		nuevo.setValor(valor)
		if self.esVacia():
			self.raiz=nuevo
		else:
			nuevo.setSiguiente(self.raiz)
			self.raiz=nuevo

	def pop(self):
		if self.esVacia():
			return "Esta vacia"
		else:
			res=self.raiz.getValor()
			self.raiz=self.raiz.getSiguiente()
			return res
		

	def listar(self):
		aux=self.raiz
		i=0
		mostrar=""
		while aux!=None:
			mostrar = mostrar + str(aux.getValor()) + " ---> "
			aux=aux.getSiguiente()
			i+=1
		return mostrar