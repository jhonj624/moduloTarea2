# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
import Flujos
from FlujosStep import *
import sys


class Step5(ctk.ctkWorkflowWidgetStep):
    
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
            
    def onEntry(self, comingFrom, transitionType):
        
        super(Step5, self).onEntry(comingFrom, transitionType)
        self.ctimer = qt.QTimer()
        self.ctimer.singleShot(0, self.killButton)
        
    def onExit(self, goingTo, transitionType):

        super(Step5, self).onExit(goingTo, transitionType)
        
    
    def validate(self, desiredBranchId):

        if self.trayectoriaLibreButton.isChecked():
          desiredBranchId = 'pass'
        if self.trayectoriaProgramadaButton.isChecked():
          desiredBranchId = 'fail'
        super(Step5, self).validate(True, desiredBranchId)

    def killButton(self):

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
