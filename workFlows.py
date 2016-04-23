# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer

import Flujos

class workFlows:

  def __init__(self, parent):
    parent.title = "Flujo de trabajo"
    parent.categories = ["Ejemplos"]
    parent.dependencies = []
    parent.contributors = ["Camilo Quiceno Q"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    Este modulo es para aprender a manejar flujos de trabajo
    """
    parent.acknowledgementText = """
    Desarrollado por Camilo Quiceno 
    """ # replace with organization, grant and thanks.
    self.parent = parent


class workFlowsWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):

  	self.Step1 = Flujos.Step1('Step1')
  	self.Step2 = Flujos.Step2('Step2')

  	steps = []
	steps.append(self.Step1)
	steps.append(self.Step2)

	self.workflow = ctk.ctkWorkflow()
	workflowWidget = ctk.ctkWorkflowStackedWidget()
	workflowWidget.setWorkflow(self.workflow)


	for i in xrange(len(steps) - 1):
	    self.workflow.addTransition(steps[i], steps[i + 1])

	self.workflow.start()
	workflowWidget.visible = True
	self.layout.addWidget( workflowWidget )







	

  	