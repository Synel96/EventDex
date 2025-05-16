from PyQt6.QtGui import QFont

class Design:
    BG_COLOR = "#1e2a38"
    ACCENT_COLOR = "#1abc9c"
    TEXT_COLOR = "#ecf0f1"
    INPUT_BG_COLOR = "#34495e"
    HOVER_COLOR = "#16a085"

    TITLE_FONT = QFont("Segoe UI", 24, QFont.Weight.Bold)
    LABEL_STYLE = f"color: {TEXT_COLOR}; font-weight: bold;"

    INPUT_STYLE = f"""
        background-color: {INPUT_BG_COLOR};
        color: {TEXT_COLOR};
        border: 1px solid {ACCENT_COLOR};
        border-radius: 4px;
        padding: 5px;
    """

    BUTTON_STYLE = f"""
        QPushButton {{
            background-color: {ACCENT_COLOR};
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 20px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {HOVER_COLOR};
        }}
    """

    INFOBOX_STYLE = """
        QLabel{color: white;}
        QMessageBox {background-color: #2c3e50;}
    """