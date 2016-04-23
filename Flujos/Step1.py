# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Step1(ctk.ctkWorkflowWidgetStep) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( '1. Seleccion de perfil')
           
    def createUserInterface(self):

        font =qt.QFont("Sans Serif", 12, qt.QFont.Bold)

        self.__layout = qt.QFormLayout( self )
        self.__layout.addRow(" ",qt.QWidget())
        self.__layout.addRow(" ",qt.QWidget())
        
        self.nombreBienvenida = qt.QLabel("Quien eres?")
        self.nombreBienvenida.setFont(font)
        self.__layout.addRow(self.nombreBienvenida)
        self.__layout.addRow(" ",qt.QWidget())
        self.__layout.addRow(" ",qt.QWidget())
        self.__layout.addRow(" ",qt.QWidget())
        self.EstudianteButton = qt.QRadioButton('Soy estudiante')
        self.EstudianteButton.setFont(font)
        self.ProfesorButton = qt.QRadioButton('Soy profesor')
        self.ProfesorButton.setFont(font)
        self.__layout.addRow(self.EstudianteButton)
        self.__layout.addRow(" ",qt.QWidget())
        self.__layout.addRow(self.ProfesorButton)

        qt.QTimer.singleShot(0, self.killButton)

  
    def onEntry(self, comingFrom, transitionType):
        super(Step1, self).onEntry(comingFrom, transitionType)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step1, self).onExit(goingTo, transitionType)
        print goingTo

    
    def validate(self, desiredBranchId):
        if self.EstudianteButton.isChecked():
          desiredBranchId = 'pass'
        if self.ProfesorButton.isChecked():
          desiredBranchId = 'fail'
        super(Step1, self).validate(True, desiredBranchId)
        


    def killButton(self):
        # hide useless button
        bl = slicer.util.findChildren(text='Step4')
        bl[0].hide()

