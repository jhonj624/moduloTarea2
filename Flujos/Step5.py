# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Step5(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( 'Menu estudiante'  )
        
    def createUserInterface(self):

        font =qt.QFont("Sans Serif", 12, qt.QFont.Bold)

        self.__layout = qt.QFormLayout( self )
        self.trayectoriaLibreButton = qt.QRadioButton('Trayectoria libre')
        self.trayectoriaProgramadaButton = qt.QRadioButton('Trayectoria programada')
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())

        self.trayectoriaLibreButton.setFont(font)
        self.trayectoriaProgramadaButton.setFont(font)

        self.__layout.addRow(self.trayectoriaLibreButton)
        self.__layout.addRow(self.trayectoriaProgramadaButton)

        qt.QTimer.singleShot(0, self.killButton)

    
    def onEntry(self, comingFrom, transitionType):
        super(Step5, self).onEntry(comingFrom, transitionType)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step5, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        if self.trayectoriaLibreButton.isChecked():
          desiredBranchId = 'pass'
        if self.trayectoriaProgramadaButton.isChecked():
          desiredBranchId = 'fail'
        super(Step5, self).validate(True, desiredBranchId)
        print('Validate - step %s' % self.id())

    def killButton(self):
        # hide useless button
        bl = slicer.util.findChildren(text='Step5' )
        b2 = slicer.util.findChildren(text='Step4' )
        bl[0].hide()
        b2[0].hide()
