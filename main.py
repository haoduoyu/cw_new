
import sys
from view import main_view
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # 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
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = main_view.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

