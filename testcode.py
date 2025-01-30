from PyQt6.QtWidgets import *

print("QAction in dir():", 'QAction' in dir())
print("QAction in QtWidgets:", 'QAction' in dir(QAction.__module__))