# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Step4(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( 'Menu profesor '  )
        
    def createUserInterface(self):

        font =qt.QFont("Sans Serif", 12, qt.QFont.Bold)

        self.__layout = qt.QFormLayout( self )
        self.anadirTrayectoriaButton = qt.QRadioButton('Anadir trayectoria')
        self.calificarButton = qt.QRadioButton('Calificar trayectoria de alumnos')
        self.verActividadButton = qt.QRadioButton('Ver actividad de alumnos')
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())

        self.anadirTrayectoriaButton.setFont(font)
        self.calificarButton.setFont(font)
        self.verActividadButton.setFont(font)

        self.__layout.addRow(self.anadirTrayectoriaButton)
        self.__layout.addRow(self.calificarButton)
        self.__layout.addRow(self.verActividadButton)

        qt.QTimer.singleShot(0, self.killButton)
    
    def onEntry(self, comingFrom, transitionType):
        super(Step4, self).onEntry(comingFrom, transitionType)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step4, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        if self.anadirTrayectoriaButton.isChecked():
          desiredBranchId = '1'
        if self.calificarButton.isChecked():
          desiredBranchId = '2'
        if self.verActividadButton.isChecked():
          desiredBranchId = '3'
        super(Step4, self).validate(True, desiredBranchId)
        print('Validate - step %s' % self.id())

    def killButton(self):
        # hide useless button
        bl = slicer.util.findChildren(text='Step5' )
        b2 = slicer.util.findChildren(text='Step4' )
        bl[0].hide()
        b2[0].hide()
