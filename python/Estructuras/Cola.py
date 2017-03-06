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

#from graphviz import Digraph

class Cola:
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


	def graficar2(self):
		aux=self.inicio
		datos=""
		i=0
		datos=" "+str(i)+" [label= "+str(aux.getValor())+"]  \n"

		while aux!=None:
			aux2=aux.getSiguiente()
			if aux2!=None:
				i+=1
				datos=datos+" "+str(i)+" [label= "+str(aux.getSiguiente().getValor())+"] \n"

				datos=datos +  " "+str(i-1)+" -> "+str(i)+""+" \n"
			aux=aux.getSiguiente()
		return datos

	def graficar(self):
		g2=Digraph(format='png')
		aux=self.inicio
		i=0
		g2.node( "'"+str(i)+"'",str(aux.getValor()) )
		while aux!=None:
			
			aux2=aux.getSiguiente()

			if aux2!=None:
				i+=1
				g2.node( "'"+str(i)+"'",str(aux.getSiguiente().getValor()))
				g2.edge( "'"+str(i-1)+"'","'"+str(i)+"'")
			aux=aux.getSiguiente()
		g2=apply_styles(g2,styles)
		g2.render('reportes/cola')

def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

styles = {
			'graph': {
		    	'fontsize': '16',
		   		'rankdir': 'LR',
		    },
		    'nodes': {
		        'shape': 'circle',
		        'color': 'lightblue',
		        'style': 'filled',
		        'fillcolor': '#EEEEEE',
		    },
		    'edges': {

		        'color': '#31CEF0',
		    }
		}
