from PyQt5 import QtWidgets

from g import Ui_MainWindow
from ham.beacon.beacons import beacons


class g2(Ui_MainWindow):

    def __init__(self):
        junk=1
        Ui_MainWindow.__init__(self)
        dx = beacons()
        #dx.SetBand(int(sys.argv[1]))
        dx.beacon_start(timeout=5000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = g2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
