from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QHBoxLayout,
    QSizePolicy,
    QGridLayout,
    QMessageBox,
)
from PyQt6.QtCore import Qt

import sys
import random


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.add_widgets()

    def init_ui(self):
        self.setWindowTitle("2048: Start Game")
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(400, 200, 400, 200)
        self.bottom_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.bottom_layout)

    def add_widgets(self):
        self.heading_label = QLabel("2048")
        self.heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading_font = self.heading_label.font()
        heading_font.setPointSize(20)
        self.heading_label.setFont(heading_font)
        self.main_layout.addWidget(self.heading_label)

        self.start_game_button = QPushButton("Start Game!")
        self.start_game_button.clicked.connect(
            lambda: print("[LOG] Start Game button clicked")
        )
        self.start_game_button.clicked.connect(self.start_game)

        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["", "3x3", "4x4", "5x5", "6x6"])
        self.mode_selector.currentIndexChanged.connect(
            lambda index: print(f"[LOG] {self.mode_selector.itemText(index)} selected")
        )

        self.start_game_button.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.mode_selector.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )

        self.bottom_layout.addWidget(self.start_game_button)
        self.bottom_layout.addWidget(self.mode_selector)

    def start_game(self):
        if self.mode_selector.currentIndex() < 1:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setText("Please select a mode in the dropdown.")
            msg_box.setWindowTitle("Error")
            msg_box.exec()
        else:
            self.game_window = GameWindow(self.mode_selector.currentIndex())
            self.game_window.show()
            self.close()


class GameWindow(QWidget):
    def __init__(self, mode):
        super().__init__()
        self.score = 0
        self.grid_size = self.get_grid_size(mode)
        self.init_ui()
        self.initialize_playboard()
        self.add_widgets()

    def get_grid_size(self, mode):
        if mode:
            return mode + 2

    def init_ui(self):
        self.setWindowTitle(f"2048: {self.grid_size}x{self.grid_size}")
        self.main_layout = QVBoxLayout()
        self.options_layout = QHBoxLayout()
        self.game_layout = QGridLayout()
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.options_layout)
        self.main_layout.addLayout(self.game_layout)

    def add_widgets(self):
        heading_label = QLabel("Join the numbers and get to the 2048 tile!")
        heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(heading_label)

        new_game_button = QPushButton("New Game")
        new_game_button.clicked.connect(lambda: print("[LOG] New Game button clicked"))
        new_game_button.clicked.connect(self.initialize_playboard)
        self.options_layout.addWidget(new_game_button)

        self.score_label = QLabel(f"Score: 0")
        self.options_layout.addWidget(self.score_label)

        highscore_label = QLabel("Highscore:")
        self.options_layout.addWidget(highscore_label)

        # test_spawn_button = QPushButton("Test Spawn")
        # test_spawn_button.clicked.connect(self.spawn_random_tile)
        # self.options_layout.addWidget(test_spawn_button)

    def initialize_playboard(self):
        self.playboard = []
        for row in range(self.grid_size):
            row_tiles = []
            for col in range(self.grid_size):
                print(f"[LOG] Initialized Label at {row},{col} in grid")
                tile_label = QLabel("0")
                tile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                tile_label.setStyleSheet(
                    "background: #D3D3D3; border: 2px solid #979797; "
                    "border-radius: 10px; color: #000000 "
                )
                row_tiles.append(tile_label)
                self.game_layout.addWidget(tile_label, row, col)
            self.playboard.append(row_tiles)
        self.spawn_random_tile()

        # self.set_tile_value(0,1,"5")
        # print(self.get_tile_value(0,1))

    def get_tile_value(self, row: int, col: int) -> int:
        return int(self.playboard[row][col].text())

    def set_tile_value(self, row: int, col: int, value: int):
        color = self.get_tile_color(value)
        self.playboard[row][col].setText(str(value))
        self.playboard[row][col].setStyleSheet(
            f"background: {color}; border: 2px solid #979797; "
            "border-radius: 10px; color: #000000 "
        )

    def spawn_random_tile(self):
        empty_tiles = [
            (row, col)
            for row in range(self.grid_size)
            for col in range(self.grid_size)
            if self.get_tile_value(row, col) == 0
        ]
        if not empty_tiles:
            print("[LOG] No empty tiles available.")
            return
        row, col = random.choice(empty_tiles)
        if random.random() < 0.9:
            value = 2
        else:
            value = 4
        print(f"[LOG] Set tile at {row},{col} to {value}")
        self.set_tile_value(row, col, value)

    def get_tile_color(self, value):
        colors = {
            0: "#D3D3D3",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
        }
        return colors.get(value, "black")

    def in_bounds(self, row, col):
        return 0 <= row < self.grid_size and 0 <= col < self.grid_size

    def move_tiles(self, direction):
        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        if direction not in directions:
            print("[ERROR] Invalid direction")
            return

        direction_row, direction_col = directions[direction]
        moved = False
        merged = [[False] * self.grid_size for _ in range(self.grid_size)]

        rows = (
            range(self.grid_size)
            if direction_row >= 0
            else range(self.grid_size - 1, -1, -1)
        )
        cols = (
            range(self.grid_size)
            if direction_col >= 0
            else range(self.grid_size - 1, -1, -1)
        )

        for row in rows:
            for col in cols:
                self.temp_value = self.get_tile_value(row, col)
                if self.temp_value == 0:
                    continue

                temp_row, temp_col = row, col

                while True:
                    next_row = temp_row + direction_row
                    next_col = temp_col + direction_col

                    if not self.in_bounds(next_row, next_col):
                        break

                    next_value = self.get_tile_value(next_row, next_col)

                    if next_value == 0:
                        self.set_tile_value(next_row, next_col, self.temp_value)
                        self.set_tile_value(temp_row, temp_col, 0)
                        temp_row, temp_col = next_row, next_col
                        moved = True
                    elif (
                        next_value == self.temp_value and not merged[next_row][next_col]
                    ):
                        self.set_tile_value(next_row, next_col, 2 * self.temp_value)
                        self.set_tile_value(temp_row, temp_col, 0)
                        merged[next_row][next_col] = True
                        if merged[next_row][next_col] == True:
                            self.update_score()
                        moved = True
                        break
                    else:
                        break

        if moved:
            self.spawn_random_tile()
            print("[LOG] Tiles moved and new tile spawned.")
        else:
            print("[LOG] No tiles moved.")

            # All ocuppied tiles are in this list
            tiles = [
                (row, col)
                for row in range(self.grid_size)
                for col in range(self.grid_size)
                if self.get_tile_value(row, col) != 0
            ]
            print(f"[LOG] {len(tiles)} tiles are occupied")

    def update_score(self) -> None:

        self.score += self.temp_value * 2
        self.score_label.setText(f"Score: {self.score}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_W:
            print("[LOG] 'W' Key pressed")
            self.move_tiles("up")
        elif event.key() == Qt.Key.Key_S:
            print("[LOG] 'S' Key pressed")
            self.move_tiles("down")
        elif event.key() == Qt.Key.Key_A:
            print("[LOG] 'A' Key pressed")
            self.move_tiles("left")
        elif event.key() == Qt.Key.Key_D:
            print("[LOG] 'D' Key pressed")
            self.move_tiles("right")
        else:
            super().keyPressEvent(event)


def main():
    guide()
    github_repo()
    launchWindow()

def launchWindow():
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
    
def guide():
    print("[INFO] For a detailed guide look at the README file in the project directory")
    
def github_repo():
    print("[INFO] Take a look at the github repo for this project to downlad an portable executable of the game!")
    print("[INFO] Link: https://github.com/TangenteLakai/2048-Python-PyQt6-Project")
    
    
if __name__ == "__main__":
    main()

