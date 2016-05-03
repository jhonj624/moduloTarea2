# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy
from os import listdir
from os.path import isfile, join

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
        self.mypath="C:\Users\Camilo_Q\Documents\GitHub\workFlows\Cursos" #Se crea path para busqueda de cursos
        self.onlyfiles = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))] #Lista los archivos que estan dentro del path
        for curso in self.onlyfiles: #Muestra en el comboBox de cursos los archivos que estan presentes en el path
            self.cursoRegistroComboBox.addItem(curso)
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
        
        if self.vinculoComboBox.currentIndex == 0:
            if (self.contra == self.contra1) and (self.name != " ") :
                i=1
                m=1
                curso=str(self.cursoRegistroComboBox.currentText)
                while i!=0:
                    try:   
                        filepath="C:\Users\Camilo_Q\Documents\GitHub\workFlows\Cursos/"+curso
                        rb=open_workbook(filepath)
                        wb = copy(rb)
                        first_sheet=rb.sheet_by_index(0)
                        a=first_sheet.row_values(i)
                        i=i+1
                        m=m+1  
                        print "Ingreso a try"
                    except(IndexError):
                        i=0
                        print m

                if(i==0):
                    wb.get_sheet(0).write(m,0,self.name)
                    wb.get_sheet(0).write(m,1,self.contra)
                    wb.save(filepath)
                    print "Registro realizado en" + curso
                
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



