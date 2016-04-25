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
  	self.Step3 = Flujos.Step3('Step3')
  	self.Step4 = Flujos.Step4('Step4')
  	self.Step5 = Flujos.Step5('Step5')
  	self.Step6 = Flujos.Step6('Step6')
  	self.Step7 = Flujos.Step7('Step7')
  	self.Step8 = Flujos.Step8('Step8')
  	self.Step9 = Flujos.Step9('Step9')
  	self.Step10 = Flujos.Step10('Step10')

  	steps = []
	steps.append(self.Step1)
	steps.append(self.Step2)
	steps.append(self.Step3)
	steps.append(self.Step4)
	steps.append(self.Step5)
	steps.append(self.Step6)
	steps.append(self.Step7)
	steps.append(self.Step8)
	steps.append(self.Step9)
	steps.append(self.Step10)

	self.workflow = ctk.ctkWorkflow()
	workflowWidget = ctk.ctkWorkflowStackedWidget()
	workflowWidget.setWorkflow(self.workflow)
	
	self.workflow.addTransition(self.Step1, self.Step2, 'pass', ctk.ctkWorkflow.Bidirectional )
	self.workflow.addTransition(self.Step1, self.Step3, 'fail', ctk.ctkWorkflow.Bidirectional )
	self.workflow.addTransition(self.Step3, self.Step4)
	self.workflow.addTransition(self.Step2, self.Step5)
	self.workflow.addTransition(self.Step5, self.Step6, 'pass', ctk.ctkWorkflow.Bidirectional )
	self.workflow.addTransition(self.Step5, self.Step7, 'fail', ctk.ctkWorkflow.Bidirectional )
	self.workflow.addTransition(self.Step4, self.Step8, '1', ctk.ctkWorkflow.Bidirectional )
	self.workflow.addTransition(self.Step4, self.Step9, '2', ctk.ctkWorkflow.Bidirectional )
	self.workflow.addTransition(self.Step4, self.Step10, '3', ctk.ctkWorkflow.Bidirectional )
	
	self.workflow.start()
	workflowWidget.visible = True
	self.layout.addWidget( workflowWidget ) 	