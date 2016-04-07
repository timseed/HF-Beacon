from PyQt5 import QtCore, QtGui, QtWidgets
from beacons import *
import logging

#This code requires QT


class qtbeacon(QtCore.QObject,beacons):
    """
    Same as the beacon class however this emits a signal called BEACON

    Note: This needs to inherit from 2 classes and the emit need to be of type QObject else it does not like to play
    """

    BEACON = QtCore.pyqtSignal(list)

    def getstation(self):
        """
        Send the Array via a QT Signal so other objects can pick it up
        Return the list
        :return:
        """
        next_station = super(qtbeacon,self).getstation()
        logger.debug("Emit BEACON")
        self.BEACON.emit(next_station)
        return next_station

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    dx = qtbeacon()
    #dx.SetBand(int(sys.argv[1]))
    dx.run(timeout=5000)
    # dx.dump_band(4)
    junk=1
    junk=1
