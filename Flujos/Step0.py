# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
import xlrd

class Step0(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( 'Registro'  )
        
    def createUserInterface(self):

        font =qt.QFont("Sans Serif", 12, qt.QFont.Bold)

        self.__layout = qt.QFormLayout( self )
        self.__layout.addRow(" ",qt.QWidget())
       
        self.nombreRegistro = qt.QLabel("Nombre: ")
        self.nombreRegistroTextEdit = qt.QLineEdit()
        self.nombreRegistroTextEdit.setFixedWidth(200)
        self.nombreRegistroTextEdit.textChanged.connect(self.textchanged1)
        self.__layout.addRow(self.nombreRegistro,self.nombreRegistroTextEdit)

        self.contrasenaRegistro = qt.QLabel("Contrasena: ")
        self.contrasenaRegistroTextEdit = qt.QLineEdit()
        self.contrasenaRegistroTextEdit.setFixedWidth(200)
        self.contrasenaRegistroTextEdit.setEchoMode(qt.QLineEdit.Password)
        self.contrasenaRegistroTextEdit.textChanged.connect(self.textchanged2)
        self.__layout.addRow(self.contrasenaRegistro,self.contrasenaRegistroTextEdit)

        self.contrasenaRegistro1 = qt.QLabel("Repetir contrasena: ")
        self.contrasenaRegistro1TextEdit = qt.QLineEdit()
        self.contrasenaRegistro1TextEdit.setFixedWidth(200)
        self.contrasenaRegistro1TextEdit.setEchoMode(qt.QLineEdit.Password)
        self.contrasenaRegistro1TextEdit.textChanged.connect(self.textchanged3)
        self.__layout.addRow(self.contrasenaRegistro1,self.contrasenaRegistro1TextEdit)

        self.vinculoRegistro = qt.QLabel("Tipo de vinculo: ")
        self.vinculoComboBox = qt.QComboBox()
        self.vinculoComboBox.addItem('Estudiante')
        self.vinculoComboBox.addItem('Profesor')
        self.__layout.addRow(self.vinculoRegistro,self.vinculoComboBox)

        self.cursoRegistro = qt.QLabel('Curso al que pertenece')
        self.cursoRegistroComboBox = qt.QComboBox()
        self.cursoRegistroComboBox.addItem('0123345')
        self.__layout.addRow(self.cursoRegistro,self.cursoRegistroComboBox)

        self.__layout.addRow(" ",qt.QWidget())

        self.botonRegistro = qt.QPushButton('Realizar Registro')
        self.botonRegistro.connect('clicked(bool)',self.onApplyRegistro)

        self.botonReiniciarRegistro = qt.QPushButton('Reiniciar Registro')
        self.botonReiniciarRegistro.connect('clicked(bool)',self.onApplyReiniciarRegistro)
        self.__layout.addRow(self.botonRegistro)
        self.__layout.addRow(self.botonReiniciarRegistro)

        
    def onEntry(self, comingFrom, transitionType):
        self.ctimer = qt.QTimer()
        self.ctimer.singleShot(0, self.killButton)
        super(Step0, self).onEntry(comingFrom, transitionType)
        
    def onExit(self, goingTo, transitionType):
        super(Step0, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        validationSuceeded = True
        super(Step0, self).validate(validationSuceeded, desiredBranchId)
        print('Validate - step %s' % self.id())

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

    def textchanged1(self,text):
        self.name = text

    def textchanged2(self,text):
        self.contra = text

    def textchanged3(self,text):
        self.contra1 = text

    def onApplyRegistro(self):
        print "Registro realizado"
        if self.vinculoComboBox.currentIndex == 0:
            if (self.contra == self.contra1) and (self.name != " ") :
                print "Registro exitoso"
                book=xlrd.open_workbook("C:\Users\Camilo_Q\Documents\GitHub\workFlows\Cursos\Lista1.xlsx")
                
            else:
                qt.QMessageBox.critical(slicer.util.mainWindow(),'Error de registro', 'Intente de nuevo')

        else:
            if (self.contra == self.contra1):
                print "Registro exitoso"
            else:
                qt.QMessageBox.critical(slicer.util.mainWindow(),'Error de registro', 'Intente de nuevo')

    def onApplyReiniciarRegistro(self):
        print "Reinicio de registro"
        self.nombreRegistroTextEdit.setText("")
        self.contrasenaRegistro1TextEdit.setText("")
        self.contrasenaRegistroTextEdit.setText("")

