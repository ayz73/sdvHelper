import sys

from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QHBoxLayout, QLabel, 
                             QMainWindow, QToolBar, QVBoxLayout, QWidget,
                             QTabWidget)


class SdvHelper(QMainWindow):
    """Create the main window that has all the widgets"""

    def __init__(self):
        """Initialize the settings of the main window"""
        super(SdvHelper, self).__init__()
        self.resize(800, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle("sdvHelper")
        self.setWindowIcon(QIcon("sdvhelper\icons\icon.ico"))

        self.main_ui()
        self.show()
    
    def main_ui(self):
        """Create the main parts of the ui"""
        self.create_main_tabs()

    def create_main_tabs(self):
        """Create the tabs for switching content"""
        self.main_tabs = QTabWidget()
        self.setCentralWidget(self.main_tabs)

        self.farming_tab = QWidget()
        self.villagers_tab = QWidget()
        self.collections_tab = QWidget()

        self.main_tabs.addTab(self.farming_tab, "Farming")
        self.main_tabs.addTab(self.villagers_tab, "Villagers")
        self.main_tabs.addTab(self.collections_tab, "Collections")


def main():
    """Opens the main window"""
    application = QApplication(sys.argv)
    window = SdvHelper()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
