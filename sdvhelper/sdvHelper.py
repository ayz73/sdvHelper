import sys

from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QHBoxLayout, QLabel, 
                             QMainWindow, QToolBar, QVBoxLayout, QWidget,
                             QTabWidget, QTableWidget, QAbstractItemView)


class SdvHelper(QMainWindow):
    """Create the main window that has all the widgets"""

    def __init__(self):
        """Initialize the settings of the main window"""
        super().__init__()
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

        self.main_tabs.addTab(FarmingTab(), "Farming")
        self.main_tabs.addTab(VillagersTab(), "Villagers")
        self.main_tabs.addTab(CollectionsTab(), "Collections")


class FarmingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.create_layout()
        self.create_table()

    def create_layout(self):
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

    def create_table(self):
        self.selection_table = QTableWidget()
        self.selection_table.setColumnCount(2)
        self.selection_table.setRowCount(3)
        self.selection_table.horizontalHeader().setVisible(False)
        self.selection_table.verticalHeader().setVisible(False)
        self.selection_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.main_layout.addWidget(self.selection_table)


class VillagersTab(QWidget):
    pass


class CollectionsTab(QWidget):
    pass


def main():
    """Opens the main window"""
    application = QApplication(sys.argv)
    window = SdvHelper()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
