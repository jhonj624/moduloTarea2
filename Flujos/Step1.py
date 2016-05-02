# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer

import Flujos


class Step1(ctk.ctkWorkflowWidgetStep) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( 'Seleccion de perfil')
           
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
        self.EstudianteButton = qt.QRadioButton('Soy estudiante')
        self.EstudianteButton.setFont(font)
        self.ProfesorButton = qt.QRadioButton('Soy profesor')
        self.ProfesorButton.setFont(font)
        self.soyNuevoButton = qt.QRadioButton('Soy nuevo')
        self.soyNuevoButton.setFont(font)
        self.__layout.addRow(self.EstudianteButton)
        self.__layout.addRow(" ",qt.QWidget())
        self.__layout.addRow(self.ProfesorButton)
        self.__layout.addRow(" ",qt.QWidget())
        self.__layout.addRow(self.soyNuevoButton)
  
    def onEntry(self, comingFrom, transitionType):
        self.ctimer = qt.QTimer()
        self.ctimer.singleShot(0, self.killButton)
        
        super(Step1, self).onEntry(comingFrom, transitionType)
        
    def onExit(self, goingTo, transitionType):
        super(Step1, self).onExit(goingTo, transitionType)
        print goingTo
    
    def validate(self, desiredBranchId):
        if self.EstudianteButton.isChecked():
          desiredBranchId = 'pass'
        if self.ProfesorButton.isChecked():
          desiredBranchId = 'fail'
        if self.soyNuevoButton.isChecked():
          desiredBranchId = 'Reg'
        super(Step1, self).validate(True, desiredBranchId)
        
    def killButton(self):
        # hide useless button
        bl = slicer.util.findChildren(text='Step6' )
        b2 = slicer.util.findChildren(text='Step7' )
        b3 = slicer.util.findChildren(text='Step8' )
        b4 = slicer.util.findChildren(text='Step9' )
        b5 = slicer.util.findChildren(text='Step10' )
        b6 = slicer.util.findChildren(text='Step0' )

        bl[0].hide()
        b2[0].hide()
        b3[0].hide()
        b4[0].hide()
        b5[0].hide()
        b6[0].hide()


