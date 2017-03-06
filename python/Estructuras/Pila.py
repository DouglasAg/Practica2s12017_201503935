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

#import graphviz as gv

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

	def graficar2(self):
		aux=self.raiz
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
		g2=gv.Digraph(format='png')
		aux=self.raiz
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
		g2.render('reportes/pila')

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

