

class FlujosStep() :


	  def cursoFuncion(self, parameterNode):
	    '''
	    Keep the pointer to the parameter node for each step
	    '''
	    self.__curso = parameterNode

	  def cursoMostrar(self):
	    return self.__curso