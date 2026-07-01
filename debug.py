import pygame
import ui

class DebugInfo:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.per_row_height = 30
        self.margin_bottom = 10
        self.info = {}
        self.delay = 0.1
        self.delay_timer = 0

    def add_info(self, info_name, info_value):
        label = ui.Label(self.window, (0, 0), f"{info_name}: {info_value}", font_px=self.per_row_height)
        x = 10
        y = len(self.info) * label.get_font().get_height() + self.margin_bottom
        label.set_pos(x, y)
        self.info[info_name] = {
            "value": info_value,
            "label": label
            }

    def set_info_value(self, info_name, info_value):
        self.info[info_name]["value"] = info_value
        self.info[info_name]["label"].set_text(f"{info_name}: {info_value}")

    def debug_render(self, color):
        for info in self.info:
            self.info[info]["label"].render(color)
