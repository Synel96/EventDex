import sys
import os
import pandas as pd
from ui_design import Design
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QDateEdit, QComboBox, QSpinBox, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QDate


class EventDexApp(QWidget):
    VERSION = "v0.1 MVP"
    AUTHOR = "Synel96"

    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_ui()

    def setup_window(self):
        self.setWindowTitle(f"Event Dex {self.VERSION} by: {self.AUTHOR}")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(f"background-color: {Design.BG_COLOR};")
        self.setWindowIcon(QIcon("favicon.ico"))

    def setup_ui(self):
        # Title label
        self.title_label = QLabel("EventDex")
        self.title_label.setFont(Design.TITLE_FONT)
        self.title_label.setStyleSheet(f"color: {Design.ACCENT_COLOR};")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFixedHeight(50)

        # Inputs
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.style_input_widget(self.date_input)

        self.event_type_input = QComboBox()
        self.event_type_input.addItems([
            "Max Monday", "Spotlight Hour", "Raid Hour",
            "Community Day", "Raid Day", "Go Fest", "Go Tour", "Other"
        ])
        self.style_input_widget(self.event_type_input)

        self.attendee_input = QSpinBox()
        self.attendee_input.setRange(0, 10000)
        self.attendee_input.setValue(1)
        self.style_input_widget(self.attendee_input)

        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("Enter host name")
        self.style_input_widget(self.host_input)

        # Labels
        self.date_label = self.create_label("Date:")
        self.event_type_label = self.create_label("Event Type:")
        self.attendee_label = self.create_label("Attendees:")
        self.host_label = self.create_label("Host:")

        # Layouts
        date_layout = self.create_row(self.date_label, self.date_input)
        event_type_layout = self.create_row(self.event_type_label, self.event_type_input)
        attendee_layout = self.create_row(self.attendee_label, self.attendee_input)
        host_layout = self.create_row(self.host_label, self.host_input)

        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.setFixedWidth(120)
        self.save_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save_button.setStyleSheet(Design.BUTTON_STYLE)
        self.save_button.clicked.connect(self.save_to_excel)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.save_button)
        button_layout.addStretch()

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.title_label)
        main_layout.addSpacing(20)
        main_layout.addLayout(date_layout)
        main_layout.addLayout(event_type_layout)
        main_layout.addLayout(attendee_layout)
        main_layout.addLayout(host_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

    def style_input_widget(self, widget):
        widget.setStyleSheet(Design.INPUT_STYLE)
        widget.setMaximumWidth(270)

    def create_label(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet(Design.LABEL_STYLE)
        lbl.setFixedWidth(80)
        return lbl

    def show_info_message(self, title, message):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Icon.Information)
        info_box.setWindowTitle(title)
        info_box.setText(message)
        info_box.setStyleSheet(Design.INFOBOX_STYLE)
        info_box.exec()

    def create_row(self, label_widget, input_widget):
        layout = QHBoxLayout()
        layout.addWidget(label_widget)
        layout.addWidget(input_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    def save_to_excel(self):
        filename = "events.xlsx"
        data = {
            "Date": [self.date_input.date().toString("yyyy-MM-dd")],
            "Event Type": [self.event_type_input.currentText()],
            "Attendees": [self.attendee_input.value()],
            "Host": [self.host_input.text()]
        }

        if os.path.exists(filename):
            try:
                df = pd.read_excel(filename)
                df_new = pd.DataFrame(data)
                df = pd.concat([df, df_new], ignore_index=True)
            except Exception as e:
                self.show_info_message("Error", f"Failed to read existing Excel file:\n{e}")
                return
        else:
            df = pd.DataFrame(data)

        try:
            df.to_excel(filename, index=False)
            self.show_info_message("Saved", "Event saved successfully!")
        except Exception as e:
            self.show_info_message("Error", f"Failed to save Excel file")