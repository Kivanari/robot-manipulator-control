from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QGroupBox,
    QLineEdit,
    QSlider,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Manipulator Control")
        self.resize(1000, 700)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный вертикальный layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # ---------- Верхняя панель ----------
        top_bar_layout = QHBoxLayout()

        title_label = QLabel("Интерфейс управления манипулятором")
        status_label = QLabel("Статус: Симуляция")
        stop_button = QPushButton("STOP")

        top_bar_layout.addWidget(title_label)
        top_bar_layout.addStretch()
        top_bar_layout.addWidget(status_label)
        top_bar_layout.addWidget(stop_button)

        main_layout.addLayout(top_bar_layout)

        # ---------- Блок подключения ----------
        connection_group = QGroupBox("Подключение к контроллеру")
        connection_layout = QGridLayout()
        connection_group.setLayout(connection_layout)

        port_label = QLabel("COM-порт:")
        baudrate_label = QLabel("Скорость:")

        self.port_input = QLineEdit("COM3")
        self.baudrate_input = QLineEdit("115200")

        self.connect_button = QPushButton("Подключить")
        self.disconnect_button = QPushButton("Отключить")
        self.scan_button = QPushButton("Сканировать порты")

        connection_layout.addWidget(port_label, 0, 0)
        connection_layout.addWidget(self.port_input, 0, 1)
        connection_layout.addWidget(baudrate_label, 1, 0)
        connection_layout.addWidget(self.baudrate_input, 1, 1)
        connection_layout.addWidget(self.connect_button, 2, 0)
        connection_layout.addWidget(self.disconnect_button, 2, 1)
        connection_layout.addWidget(self.scan_button, 3, 0, 1, 2)

        main_layout.addWidget(connection_group)

        # ---------- Блок ручного управления J1 ----------
        manual_group = QGroupBox("Ручное управление")
        manual_layout = QVBoxLayout()
        manual_group.setLayout(manual_layout)
# J1
        j1_group = QGroupBox("Ось J1")
        j1_layout = QVBoxLayout()
        j1_group.setLayout(j1_layout)

        self.j1_value_label = QLabel("Текущее положение: 0°")

        self.j1_slider = QSlider(Qt.Horizontal)
        self.j1_slider.setMinimum(-90)
        self.j1_slider.setMaximum(90)
        self.j1_slider.setValue(0)

        j1_buttons_layout = QHBoxLayout()
        self.j1_minus_button = QPushButton("J1-")
        self.j1_plus_button = QPushButton("J1+")

        j1_buttons_layout.addWidget(self.j1_minus_button)
        j1_buttons_layout.addWidget(self.j1_plus_button)

        j1_layout.addWidget(self.j1_value_label)
        j1_layout.addWidget(self.j1_slider)
        j1_layout.addLayout(j1_buttons_layout)

        manual_layout.addWidget(j1_group)
# J2 ось
        j2_group = QGroupBox("Ось J2")
        j2_layout = QVBoxLayout()
        j2_group.setLayout(j2_layout)

        self.j2_value_label = QLabel("Текущее положение: 0°")

        self.j2_slider = QSlider(Qt.Horizontal)
        self.j2_slider.setMinimum(-90)
        self.j2_slider.setMaximum(90)
        self.j2_slider.setValue(0)

        j2_buttons_layout = QHBoxLayout()
        self.j2_minus_button = QPushButton("J2-")
        self.j2_plus_button = QPushButton("J2+")

        j2_buttons_layout.addWidget(self.j2_minus_button)
        j2_buttons_layout.addWidget(self.j2_plus_button)

        j2_layout.addWidget(self.j2_value_label)
        j2_layout.addWidget(self.j2_slider)
        j2_layout.addLayout(j2_buttons_layout)

        manual_layout.addWidget(j2_group)


        # ---------- Поле шага ----------
        step_layout = QHBoxLayout()
        step_label = QLabel("Шаг перемещения:")
        self.step_input = QLineEdit("5")

        step_layout.addWidget(step_label)
        step_layout.addWidget(self.step_input)

        manual_layout.addLayout(step_layout)

        main_layout.addWidget(manual_group)

        # ---------- Заглушка ----------
        info_label = QLabel("Позже добавим J2, J3, сценарии, координаты и журнал.")
        main_layout.addWidget(info_label)

        # ---------- Связи ----------
        #J1
        self.j1_slider.valueChanged.connect(self.update_j1_label)
        self.j1_minus_button.clicked.connect(self.decrease_j1)
        self.j1_plus_button.clicked.connect(self.increase_j1)
        #J2
        self.j2_slider.valueChanged.connect(self.update_j2_label)
        self.j2_minus_button.clicked.connect(self.decrease_j2)
        self.j2_plus_button.clicked.connect(self.increase_j2)

    def update_j1_label(self, value):
        self.j1_value_label.setText(f"Текущее положение: {value}°")
    def update_j2_label(self, value):
        self.j2_value_label.setText(f"Текущее положение: {value}°")

    def get_step_value(self):
        text = self.step_input.text()
        try:
            step = int(text)
            return step
        except ValueError:
            return 1

    def decrease_j1(self):
        current_value = self.j1_slider.value()
        step = self.get_step_value()
        new_value = current_value - step
        self.j1_slider.setValue(new_value)
    def decrease_j2(self):
        current_value = self.j2_slider.value()
        step = self.get_step_value()
        new_value = current_value - step
        self.j2_slider.setValue(new_value)

    def increase_j1(self):
        current_value = self.j1_slider.value()
        step = self.get_step_value()
        new_value = current_value + step
        self.j1_slider.setValue(new_value)
    def increase_j2(self):
        current_value = self.j2_slider.value()
        step = self.get_step_value()
        new_value = current_value + step
        self.j2_slider.setValue(new_value)