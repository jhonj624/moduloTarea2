# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Step8(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( 'Anadir trayectoria'  )
        
    def createUserInterface(self):

        font =qt.QFont("Sans Serif", 12, qt.QFont.Bold)

        self.__layout = qt.QFormLayout( self )
        

        qt.QTimer.singleShot(0, self.killButton)

    
    def onEntry(self, comingFrom, transitionType):
        super(Step8, self).onEntry(comingFrom, transitionType)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step8, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        validationSuceeded = True
        super(Step8, self).validate(validationSuceeded, desiredBranchId)
        print('Validate - step %s' % self.id())

    def killButton(self):
        # hide useless button
        bl = slicer.util.findChildren(text='Step6' )
        b2 = slicer.util.findChildren(text='Step7' )
        b3 = slicer.util.findChildren(text='Step8' )
        b4 = slicer.util.findChildren(text='Step9' )
        b5 = slicer.util.findChildren(text='Step10' )

        bl[0].hide()
        b2[0].hide()
        b3[0].hide()
        b4[0].hide()
        b5[0].hide()
