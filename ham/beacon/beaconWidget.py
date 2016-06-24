from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class beaconWidget(QtWidgets.QWidget):

  def __init__(self, parent = None,call="",range=0,bearing=0,freq=123):

     QtWidgets.QWidget.__init__(self, parent)

     self.call= QLabel(str(call))
     self.range = QLabel(str(range))
     self.bearing = QLabel(str(bearing))
     self.frequency = QLabel(str(freq))

     layout = QGridLayout(self)
     layout.addWidget(self.call, 0, 0)
     layout.addWidget(self.frequency,0 , 1)
     layout.addWidget(self.range, 0,2 )
     layout.addWidget(self.bearing,0 ,3 )
