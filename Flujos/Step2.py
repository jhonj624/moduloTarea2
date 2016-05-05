# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
import xlrd
from os import listdir
from os.path import isfile, join
from FlujosStep import *
import sys

class Step2( ctk.ctkWorkflowWidgetStep , ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( '2. Log in alumno ' )
       
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

        self.cursoRegistro = qt.QLabel('Curso al que pertenece')
        self.cursoLoginComboBox = qt.QComboBox()
        self.mypath="C:\Users\Camilo_Q\Documents\GitHub\workFlows\Cursos" #Se crea path para busqueda de cursos
        self.onlyfiles = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))] #Lista los archivos que estan dentro del path
        for curso in self.onlyfiles: #Muestra en el comboBox de cursos los archivos que estan presentes en el path
            self.cursoLoginComboBox.addItem(curso)
        self.__layout.addRow(self.cursoRegistro,self.cursoLoginComboBox)
        sys.argv=["Nombre","Contrasena","Curso","Fecha"]

    def onEntry(self, comingFrom, transitionType):
        super(Step2, self).onEntry(comingFrom, transitionType)
        self.ctimer = qt.QTimer()
        self.ctimer.singleShot(0, self.killButton)
    
    def onExit(self, goingTo, transitionType):
        super(Step2, self).onExit(goingTo, transitionType)
        
                        
    def validate(self, desiredBranchId):
        i=1
        m=0
        a=['Inicio']
        self.curso=str(self.cursoLoginComboBox.currentText)
        sys.argv[2]=self.curso
        filepath="C:\Users\Camilo_Q\Documents\GitHub\workFlows\Cursos/"+self.curso
        book=xlrd.open_workbook(filepath)                
        
        while i!=0:

            try:

                first_sheet=book.sheet_by_index(0)
                a=first_sheet.row_values(i)
                print a[0]
                print a[1]
                if (self.name == a[0] and self.contra == a[1]):


                    validationSuceeded = True
                    super(Step2, self).validate(validationSuceeded, desiredBranchId)
                    m=1
                i=i+1

            except(IndexError):

                i=0
  
        if(i==0 and m!=1):

              super(Step2, self).validate(False, desiredBranchId)
              qt.QMessageBox.critical(slicer.util.mainWindow(),'Error Login', 'Usuario y/o contrasena invalidos')
                
    
    def textchanged1(self,text):
        self.name = text
        sys.argv[0]=str(self.name)
                    
                    

    def textchanged2(self,text):
        self.contra = text
        sys.argv[1]=str(self.contra)

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





