# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final01.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FantacyCricket(object):
    def setupUi(self, FantacyCricket):
        FantacyCricket.setObjectName("FantacyCricket")
        FantacyCricket.resize(955, 762)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        FantacyCricket.setFont(font)
        FantacyCricket.setAutoFillBackground(False)
        FantacyCricket.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(FantacyCricket)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(57, 57, 57)")
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color:rgb(218, 218, 218)")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.t1 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.t2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t2.setFont(font)
        self.t2.setObjectName("t2")
        self.horizontalLayout.addWidget(self.t2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.t3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t3.setFont(font)
        self.t3.setObjectName("t3")
        self.horizontalLayout.addWidget(self.t3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.t4 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t4.setFont(font)
        self.t4.setObjectName("t4")
        self.horizontalLayout.addWidget(self.t4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.widget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 8, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t5.setFont(font)
        self.t5.setObjectName("t5")
        self.horizontalLayout_3.addWidget(self.t5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t6.setFont(font)
        self.t6.setObjectName("t6")
        self.horizontalLayout_3.addWidget(self.t6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.r1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r1.setFont(font)
        self.r1.setStyleSheet("background-color:rgb(218, 218, 218)")
        self.r1.setObjectName("r1")
        self.horizontalLayout_10.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r2.setFont(font)
        self.r2.setStyleSheet("background-color:rgb(218, 218, 218)")
        self.r2.setObjectName("r2")
        self.horizontalLayout_10.addWidget(self.r2)
        self.r3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r3.setFont(font)
        self.r3.setStyleSheet("background-color:rgb(218, 218, 218)")
        self.r3.setObjectName("r3")
        self.horizontalLayout_10.addWidget(self.r3)
        self.r4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r4.setFont(font)
        self.r4.setStyleSheet("background-color:rgb(218, 218, 218)")
        self.r4.setObjectName("r4")
        self.horizontalLayout_10.addWidget(self.r4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.l1 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.verticalLayout_3.addWidget(self.l1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(200, 0))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("next1.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:rgb(218, 218, 218)")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        self.t7.setObjectName("t7")
        self.horizontalLayout_11.addWidget(self.t7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.l2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.verticalLayout_4.addWidget(self.l2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        FantacyCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FantacyCricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.menubar.setFont(font)
        self.menubar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar.setToolTip("")
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setAutoFillBackground(True)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        FantacyCricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FantacyCricket)
        self.statusbar.setObjectName("statusbar")
        FantacyCricket.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(FantacyCricket)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(FantacyCricket)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(FantacyCricket)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(FantacyCricket)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionEXIT = QtWidgets.QAction(FantacyCricket)
        self.actionEXIT.setObjectName("actionEXIT")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEXIT)
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(FantacyCricket)
        QtCore.QMetaObject.connectSlotsByName(FantacyCricket)


        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufn)


        self.bat=0
        self.bow=0
        self.wk=0
        self.ar=0
        self.ptav=1000
        self.ptusd=0

        self.r1.toggled.connect(self.checkctg)
        self.r2.toggled.connect(self.checkctg)
        self.r3.toggled.connect(self.checkctg)
        self.r4.toggled.connect(self.checkctg)

        self.l1.itemDoubleClicked.connect(self.rmlist1)
        self.l2.itemDoubleClicked.connect(self.rmlist2)



    def rmlist1(self,item):

       import sqlite3
       myteam=sqlite3.connect('cricket.db')
       curteam=myteam.cursor()
       curteam.execute("select ctg from stats where player=='"+item.text()+"';")
       ctg=curteam.fetchone()
       if self.l2.count()>=11:
           self.warn("Team is Already Full!!!")
           return
       elif int(self.t1.text())>=5 and ctg[0]=="BAT":
           self.warn("Can not select more than five batsman")
           return
       elif int(self.t2.text())>=5 and ctg[0]=="BOW":
           self.warn("Can not select more than five bowlers")
           return
       elif int(self.t3.text())>=3 and ctg[0]=="AR":
           self.warn("Can not select more than three all rounders")
           return
       elif int(self.t4.text())>=1 and ctg[0]=="WK":
           self.warn("Can not select more than one wicket keeper")
           return
       else :
           self.l1.takeItem(self.l1.row(item))
           self.l2.addItem(item.text())
           self.rmspeciality()
           import sqlite3
           myteam=sqlite3.connect('cricket.db')
           curteam=myteam.cursor()
           curteam.execute("select value from stats where player=='"+item.text()+"';")
           try:
               val=curteam.fetchone()
               self.t6.setText(str(val[0]+int(self.t6.text())))
               self.t5.setText(str(int(self.t5.text())-val[0]))
           except:
               myteam.rollback()
               warn("SQL statement Error, please Check and try again")
           
           return

    def rmlist2(self,item):
        if self.r1.isChecked()==True:
            ctgcur="BAT"
        
        elif self.r2.isChecked()==True:
            ctgcur="BOW"
            
        elif self.r3.isChecked()==True:
            ctgcur="AR"
            
        elif self.r4.isChecked()==True:
            ctgcur="WK"
        else:
            ctgcur=""


        import sqlite3
        myteam=sqlite3.connect('cricket.db')
        curteam=myteam.cursor()
        curteam.execute("select ctg from stats where player=='"+item.text()+"';")
        ctg=curteam.fetchone()
        
        self.l2.takeItem(self.l2.row(item))
        if ctg[0]==ctgcur:
            self.l1.addItem(item.text())
        self.rmspeciality()
        import sqlite3
        myteam=sqlite3.connect('cricket.db')
        curteam=myteam.cursor()
        curteam.execute("select value from stats where player=='"+item.text()+"';")
        try:
           val=curteam.fetchone()
           self.t6.setText(str(int(self.t6.text())-val[0]))
           self.t5.setText(str(int(self.t5.text())+val[0]))
        except:
           myteam.rollback()
           warn("SQL statement Error, please Check and try again")
        
        return
            
    def rmspeciality(self):
        self.bat=0
        self.bow=0
        self.wk=0
        self.ar=0
        for i in range(0,self.l2.count(),1):
                play=self.l2.item(i).text()
                import sqlite3
                myteam=sqlite3.connect('cricket.db')
                curteam=myteam.cursor()
                curteam.execute("select ctg from stats where player=='"+play+"';")
                spe=curteam.fetchone()
                ctg=spe[0]
                if ctg=="BAT":self.bat+=1
                if ctg=="BOW":self.bow+=1
                if ctg=="AR":self.ar+=1
                if ctg=="WK":self.wk+=1
        self.t1.setText(str(self.bat))
        self.t2.setText(str(self.bow))
        self.t3.setText(str(self.ar))
        self.t4.setText(str(self.wk))
        return

    
    def checkctg(self):
        self.l1.clear()
        if self.r1.isChecked()==True:
            ctg="BAT"
            
        if self.r2.isChecked()==True:
            ctg="BOW"
            
        if self.r3.isChecked()==True:
            ctg="AR"
            
        if self.r4.isChecked()==True:
            ctg="WK"
            
        if self.t7.text()=="":
            self.warn("First Select Your Team")
            return
            
        import sqlite3
        myteam=sqlite3.connect('cricket.db')
        curteam=myteam.cursor()
        curteam.execute("select player from stats where ctg=='"+ctg+"';")
        plrs=curteam.fetchall()
        player=[]
        for i in range(0,self.l2.count(),1):
            player.append(self.l2.item(i).text())
        for nm in plrs:
            if nm[0] not in player:
                self.l1.addItem(nm[0])
        return

    def menufn(self,action):
         txt=(action.text())

         if txt=="EVALUATE Team":
            self.openevaluate()
            return

         if txt=="EXIT":
             self.warn("Thank for Using the Application \n \tVisit Again!!!")
             exit()

         if txt=="New Team":
            self.l1.clear()
            self.l2.clear()
            from newteam import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()
            txt=ui.t1.text()
            self.t7.setText(txt)

            self.bat=0
            self.bow=0
            self.wk=0
            self.ar=0
            self.ptav=1000
            self.ptusd=0
            self.t5.setText(str(self.ptav))
            self.t6.setText(str(self.ptusd))
            self.t1.setText(str(self.bat))
            self.t2.setText(str(self.bow))
            self.t3.setText(str(self.ar))
            self.t4.setText(str(self.wk))
            return

        
         if txt=="Open Team":
            from select2 import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()
            txt=ui.c1.currentText()
            self.t7.setText(txt)
            import sqlite3
            myteam=sqlite3.connect('cricket.db')
            curteam=myteam.cursor()
            curteam.execute("select players from teams where name=='"+txt+"';")
            plrs=curteam.fetchone()
            self.l2.clear()
            self.l2.addItems(plrs[0].split(','))
            
            self.speciality()
            return

        
         if txt=="Save Team":
             if self.l2.count()!=11:
                 self.warn("players in the Team is not Sufficient!!!")
                 return
             if self.t7.text()=="":
                 self.warn("The Team Name can not be Empty!!")
                 return
             if self.t4.text()=='0':
                 self.warn("Minimum one Wicketkeeper is must!!!")
                 return

             players=""

             for i in range(0,self.l2.count(),1):
                 players+=self.l2.item(i).text()
                 if i!=self.l2.count()-1:
                     players+=','

             

             
                
             import sqlite3 
             myteam=sqlite3.connect("cricket.db")
             curteam=myteam.cursor()
             
             curteam.execute("INSERT INTO teams(name,players,value) VALUES(?,?,?);",(self.t7.text(),players,int(self.t6.text())))
             myteam.commit()
             
             self.warn("Team is Successfully Added!!")
             return
    
    def openevaluate(self):
            from evaluate import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

    def speciality(self):
        self.bat=0
        self.bow=0
        self.wk=0
        self.ar=0
        self.ptav=1000
        self.ptusd=0
        for i in range(0,11,1):
                play=self.l2.item(i).text()
                import sqlite3
                myteam=sqlite3.connect('cricket.db')
                curteam=myteam.cursor()
                curteam.execute("select ctg from stats where player=='"+play+"';")
                spe=curteam.fetchone()
                ctg=spe[0]
                if ctg=="BAT":self.bat+=1
                if ctg=="BOW":self.bow+=1
                if ctg=="AR":self.ar+=1
                if ctg=="WK":self.wk+=1

        curteam.execute("select value from teams where name=='"+self.t7.text()+"';")
        value=curteam.fetchone()
        self.ptusd=value[0]
        self.ptav=1000-self.ptusd
        self.t5.setText(str(self.ptav))
        self.t6.setText(str(self.ptusd))
        self.t1.setText(str(self.bat))
        self.t2.setText(str(self.bow))
        self.t3.setText(str(self.ar))
        self.t4.setText(str(self.wk))
        return

    def warn(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Message")
        ret=Dialog.exec()


    def retranslateUi(self, FantacyCricket):
        _translate = QtCore.QCoreApplication.translate
        FantacyCricket.setWindowTitle(_translate("FantacyCricket", "MainWindow"))
        self.label_7.setText(_translate("FantacyCricket", "Your Selections"))
        self.label_2.setText(_translate("FantacyCricket", "Batsmen(BAT)"))
        self.label_3.setText(_translate("FantacyCricket", "Bowlers(BOW)"))
        self.label_4.setText(_translate("FantacyCricket", "Allrounders(AR)"))
        self.label_5.setText(_translate("FantacyCricket", "Wicket-Keeper(WR)"))
        self.label_6.setText(_translate("FantacyCricket", "Points Avaliable"))
        self.label.setText(_translate("FantacyCricket", "Points Used"))
        self.r1.setText(_translate("FantacyCricket", "BAT"))
        self.r2.setText(_translate("FantacyCricket", "BOW"))
        self.r3.setText(_translate("FantacyCricket", "AR"))
        self.r4.setText(_translate("FantacyCricket", "WR"))
        self.label_8.setText(_translate("FantacyCricket", "Team Name"))
        self.menuManage_Teams.setTitle(_translate("FantacyCricket", "Manage Teams"))
        self.actionNew_Team.setText(_translate("FantacyCricket", "New Team"))
        self.actionOpen_Team.setText(_translate("FantacyCricket", "Open Team"))
        self.actionSave_Team.setText(_translate("FantacyCricket", "Save Team"))
        self.actionEVALUATE_Team.setText(_translate("FantacyCricket", "EVALUATE Team"))
        self.actionEXIT.setText(_translate("FantacyCricket", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FantacyCricket = QtWidgets.QMainWindow()
    ui = Ui_FantacyCricket()
    ui.setupUi(FantacyCricket)
    FantacyCricket.show()
    sys.exit(app.exec_())
