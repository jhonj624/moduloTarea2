# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Step3(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName('Log in Profesor')
    
    def createUserInterface(self):
        
        self.__layout = qt.QFormLayout( self )
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())
 
        self.nombreLabel = qt.QLabel("         Nombre:")
        self.nombreTextEdit = qt.QLineEdit()
        self.nombreTextEdit.setFixedWidth(200)
        self.nombreTextEdit.textChanged.connect(self.textchanged1)
        self.__layout.addRow(self.nombreLabel,self.nombreTextEdit)
        self.contrasenaLabeL =  qt.QLabel("         Password:")
        self.contrasenaTextEdit = qt.QLineEdit()
        self.contrasenaTextEdit.setFixedWidth(200)
        self.contrasenaTextEdit.setEchoMode(qt.QLineEdit.Password)
        self.contrasenaTextEdit.textChanged.connect(self.textchanged2)
        self.__layout.addRow(self.contrasenaLabeL,self.contrasenaTextEdit)

    def onEntry(self, comingFrom, transitionType):
        super(Step3, self).onEntry(comingFrom, transitionType)
        self.ctimer = qt.QTimer()
        self.ctimer.singleShot(0, self.killButton)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step3, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        if (self.name =="Profesor" and self.contra == "1111"):
          validationSuceeded = True
        else:
          validationSuceeded = False
          qt.QMessageBox.critical(slicer.util.mainWindow(),'Error Login', 'Usuario y/o contrasena invalidos')
        super(Step3, self).validate(validationSuceeded, desiredBranchId)
        print('Validate - step %s' % self.id())

    def textchanged1(self,text):
        self.name = text

    def textchanged2(self,text):
        self.contra = text

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


