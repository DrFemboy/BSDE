import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QMenuBar, QMenu, QFileDialog, QMessageBox, QStatusBar, QComboBox
)
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BSDE Text Editor")
        
        # Create the text editor
        self.texteditor = QTextEdit()
        self.setCentralWidget(self.texteditor)
        
        # Create the menu bar
        menu_bar = self.menuBar()
        
        # "File" menu
        file_menu = menu_bar.addMenu("File")
        open_action = file_menu.addAction("Open")
        open_action.triggered.connect(self.open_file)
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_file)
        file_menu.addSeparator()
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        # "Help" menu
        help_menu = menu_bar.addMenu("Help")
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about_dialog)
        
        # Status bar and font size selection
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # Dropdown list for font size selection
        font_size_combo = QComboBox()
        font_size_combo.addItems([str(size) for size in range(8, 25)])  # Font sizes from 8 to 24
        font_size_combo.setCurrentText("12")  # Default font size
        font_size_combo.currentTextChanged.connect(self.change_font_size)
        
        # Add the dropdown list to the status bar
        self.statusBar.addPermanentWidget(font_size_combo)

    def open_file(self):
        """Method to open a file"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File...", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.texteditor.setPlainText(file.read())

    def save_file(self):
        """Method to save a file"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File...", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.texteditor.toPlainText())

    def show_about_dialog(self):
        """Method to show the 'About' dialog"""
        QMessageBox.about(
            self,
            "About BSDE Text Editor",
            "BSDE Text Editor\nVersion 1.0\n\nA simple text editor built with PyQt6.\nCreated with love by BlackSystem\n:3"
        )

    def change_font_size(self, size):
        """Method to change the font size"""
        font = self.texteditor.font()
        font.setPointSize(int(size))
        self.texteditor.setFont(font)

# Create and show the main window
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()