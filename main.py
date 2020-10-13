import sys
from gui.guimanager import *


def main():
    dbm.checkconfig("config.ini")
    db = dbm.openDatabase("config.ini")
    if not db:
        print("closing app")
        return
    app = QtWidgets.QApplication([])

    window = MainWindow(app)
    window.dbref  =db
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
