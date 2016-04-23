# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Step3(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( '2. Name of %s' % self.id() )
        self.setDescription( 'This is the description of %s.' % self.id() )
    
    def createUserInterface(self):
        layout = qt.QVBoxLayout(self)
        layout.addWidget(qt.QLabel(self.id()))
    
    def onEntry(self, comingFrom, transitionType):
        super(Step3, self).onEntry(comingFrom, transitionType)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step3, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        validationSuceeded = True
        super(Step3, self).validate(validationSuceeded, desiredBranchId)
        print('Validate - step %s' % self.id())