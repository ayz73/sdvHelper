import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QHBoxLayout, QLabel, 
                             QMainWindow, QToolBar, QVBoxLayout, QWidget)


class SdvHelper(QMainWindow):
    """Create the main window that has all the widgets"""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(SdvHelper, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("sdvHelper")


def main():
    """Opens the main window"""
    application = QApplication(sys.argv)
    window = SdvHelper()
    window.show()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
