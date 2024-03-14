import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeView, QFileSystemModel, QVBoxLayout, QWidget
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Asset Browser')

        # Create a QAction
        action = QAction('Set Project Directory', self)
        action.triggered.connect(self.setProjectDirectory)

        # Create a menu bar and add the action to it
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(action)

        # Create the Asset Browser widget
        self.assetBrowserWidget = QWidget(self)
        self.setCentralWidget(self.assetBrowserWidget)
        layout = QVBoxLayout(self.assetBrowserWidget)
        self.assetTreeView = QTreeView(self.assetBrowserWidget)
        layout.addWidget(self.assetTreeView)
        self.assetModel = QFileSystemModel()
        self.assetModel.setRootPath("")
        self.assetTreeView.setModel(self.assetModel)

    def setProjectDirectory(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Set Project Directory", "", options=options)
        if directory:
            print("Project directory set to:", directory)
            self.assetModel.setRootPath(directory)
            self.assetTreeView.setRootIndex(self.assetModel.index(directory))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
