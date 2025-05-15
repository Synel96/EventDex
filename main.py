import sys
from PyQt6.QtWidgets import QApplication
from eventdex import EventDexApp  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventDexApp()
    window.show()
    sys.exit(app.exec())