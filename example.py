import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from codebox import create_code_box_widget  # Verwende die Factory-Funktion aus der Bibliothek

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Box GUI")
        self.setGeometry(100, 100, 600, 400)

        # Beispielcode für die CodeBox
        example_code = """import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('Hello, PyQt5!')
label.show()
sys.exit(app.exec_())"""

        # Erstelle und füge die CodeBox zum Hauptfenster hinzu
        self.setCentralWidget(create_code_box_widget(example_code))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
