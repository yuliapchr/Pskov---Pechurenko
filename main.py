import sys
import io
import random

from PyQt6 import uic
from PyQt6.QtCore import QPointF, QPoint
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow

templane = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>410</y>
      <width>90</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.painter = QPainter
        self.coords = []
        f = io.StringIO(templane)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.make_circle)

    def make_circle(self):
        self.painter = QPainter()
        self.painter.begin(self)
        radius = random.randint(20, 100)
        self.painter.setBrush(QColor(255, 255, 0))
        self.coords = [random.randint(0, 320), random.randint(0, 410)]
        self.painter.drawEllipse(QPoint(*self.coords), radius, radius)
        self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
