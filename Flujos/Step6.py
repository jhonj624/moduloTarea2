# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
import sys
import time

class Step6(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( 'Trayectoria libre'  )
        
    def createUserInterface(self):

        font =qt.QFont("Sans Serif", 12, qt.QFont.Bold)

        self.__layout = qt.QFormLayout( self )
        self.botonRegistro = qt.QPushButton('Realizar Registro')
        self.botonRegistro.connect('clicked(bool)',self.onApplyRegistro)
        self.__layout.addRow(self.botonRegistro)
        
    
    def onEntry(self, comingFrom, transitionType):
        super(Step6, self).onEntry(comingFrom, transitionType)
        self.ctimer = qt.QTimer()
        self.ctimer.singleShot(0, self.killButton)
        print sys.argv

    def onExit(self, goingTo, transitionType):
        super(Step6, self).onExit(goingTo, transitionType)
    
    def validate(self, desiredBranchId):
        validationSuceeded = True
        super(Step6, self).validate(validationSuceeded, desiredBranchId)
       
    def onApplyRegistro(self):
        Fecha=str(time.strftime('%d %b %y %H:%M:%S'))
        sys.argv[3]=Fecha
        print sys.argv
        carpeta = sys.argv[2]
        Nombre = sys.argv[0] +"_"+sys.argv[1] +"_"+sys.argv[2] +"_"+sys.argv[3]
        print "Se guarda en la carpeta: "+carpeta
        print "Con el nombre: " +Nombre

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
