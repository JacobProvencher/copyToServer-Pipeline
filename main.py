from PySide6 import QtWidgets
from PySide6.QtWidgets import QTreeWidgetItem, QLabel, QFileDialog
from pprint import pprint
import main_ui
import os
import shutil


class copyToServer(main_ui.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(copyToServer, self).__init__()
        self.setupUi(self)

        self.oneDrivePath = None
        self.serverPath = None

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(self.oneDrivePath)
        self.assetBrowser_treeView.setModel(self.model)
        self.assetBrowser_treeView.setRootIndex(self.model.index(self.oneDrivePath))
        self.assetBrowser_treeView.setColumnWidth(0, 300)

        self.summaryTable_treeWidget.setColumnWidth(1, 100)

        self.assetBrowserSelectedItem = None
        self.summarySelectedItem = None
        self.summary_pathList = []

        self.assetBrowser_treeView.clicked.connect(self.updateAssetBrowserSelectedItem)
        self.summaryTable_treeWidget.clicked.connect(self.updateSummarySelectedItem)
        self.add_pushButton.clicked.connect(self.addItemToSummary)
        self.remove_pushButton.clicked.connect(self.removeItemFromSummary)
        self.copyToServer_pushButton.clicked.connect(self.copyToServer)

        self.setOneDriveProject_action.triggered.connect(self.setOneDriveProject)
        self.setServerProject_action.triggered.connect(self.setServerProject)

    def setOneDriveProject(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Set Project Directory", "", options=options)
        if directory:
            self.model.setRootPath(directory)
            self.assetBrowser_treeView.setRootIndex(self.model.index(directory))
            self.oneDrivePath = directory

    def setServerProject(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Set Project Directory", "", options=options)
        if directory:
            self.serverPath = directory

    def updateAssetBrowserSelectedItem(self, index):
        self.assetBrowserSelectedItem = self.model.fileInfo(index)

    def updateSummarySelectedItem(self, index):
        self.summarySelectedItem = index.row()

    def addItemToSummary(self):
        tree_widget_item = QTreeWidgetItem([self.assetBrowserSelectedItem.fileName()])
        self.summaryTable_treeWidget.addTopLevelItem(tree_widget_item)

        self.summary_pathList.append(self.assetBrowserSelectedItem.absoluteFilePath())

        for column in range(self.summaryTable_treeWidget.columnCount()):
            self.summaryTable_treeWidget.resizeColumnToContents(column)

    def removeItemFromSummary(self):
        self.summaryTable_treeWidget.takeTopLevelItem(self.summarySelectedItem)

        self.summary_pathList.pop(self.summarySelectedItem)

    def copyFile(self, src, dst):
        if os.path.exists(dst):
            os.remove(dst)
        shutil.copy2(src, dst)

    def copyToServer(self):
        srcPaths = [f"{path}/pub/tex_export_pub" for path in self.summary_pathList]
        dstPaths = [path.replace(self.oneDrivePath, self.serverPath) for path in srcPaths]
        print("-----------------------------------------------------------------")
        for src, dst in zip(srcPaths, dstPaths):
            if not os.path.exists(dst):
                os.makedirs(dst)

            for texture in os.listdir(src):
                src_texture_path = os.path.join(src, texture)
                dst_texture_path = os.path.join(dst, texture)

                if os.path.isfile(src_texture_path):
                    self.copyFile(src_texture_path, dst_texture_path)

        print("Files copied successfully!")



if __name__== '__main__':
    app = QtWidgets.QApplication()
    qt_app = copyToServer()
    qt_app.show()
    app.exec()


