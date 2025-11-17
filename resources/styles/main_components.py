Styles = {
    'main_window': """
        QMainWindow { background-color: #c5c6d1; }
    """,
    'white_widget': """
        QWidget { background-color: white; }
    """,
    'icon_button': """
        QPushButton {
            background-color: #a0a3a1;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            border: none;
        }
        QPushButton:hover { background-color: #585c59; }
        QPushButton:pressed { background-color: #e80e17; }
    """,
    'chat_label': """
        QLabel {
            color: #08090a;
            font-size: 30px;
            font-family: 'Arial';
            font-weight: bold;
            padding-left: 5px;
        }
    """,
    'add_button': """
        QPushButton {
            background-color: #781778;
            color: white;
            border-radius: 22px;
            font-size: 14px;
            padding: 0px;
        }
        QPushButton::drop-down { border: none; width: 0px; }
        QPushButton::down-arrow { image: none; }
    """,
    'filter_button': """
        QPushButton {
            background-color: white;
            color: #736d73;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            border: none;
        }
        QPushButton:hover { background-color: white; }
        QPushButton:pressed { background-color: white; }
    """,
    'combo_box': """
        QComboBox {
            background-color: white;
            color: #736d73;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            border: none;
        }
        QComboBox::drop-down { border: none; width: 0px; }
        QComboBox::down-arrow { image: none; }
        QComboBox QAbstractItemView { border: 1px solid #631454; border-radius: 10px; background-color: #d6c7d3; selection-background-color: #edcae6; padding: 5px; font-size: 16px; }
    """,
    'search_input': """
        QLineEdit {
            background-color: #FFFFFF;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 15px;
            font-size: 18px;
            color: #333333;
        }
    """,
    'info_widget': """
        QWidget { background-color: #c2bfb8; }
    """,
    'name_button': """
        QPushButton {
            color: #08090a;
            font-size: 30px;
            font-family: 'Arial';
            font-weight: bold;
            padding-left: 15px;
        }
    """,
    'chat_lists': """
        QWidget { background-color: #2C2F3F; border-radius: 12px; padding: 8px; border: 1px solid #631454;}
        QLabel  { color: white; }
    """
}