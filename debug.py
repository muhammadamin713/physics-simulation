import pygame
import ui

class DebugInfo:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.per_row_height = 30
        self.margin_bottom = 10
        self.info = {}

    def add_info(self, info_name, info_value):
        x = 10
        y = len(self.info) * self.per_row_height + self.margin_bottom
        self.info[info_name] = {
            "value": info_value,
            "label": ui.Label(self.window, (x, y), f"{info_name}: {info_value}", font_px=self.per_row_height)
            }

    def set_info_value(self, info_name, info_value):
        self.info[info_name]["value"] = info_value
        self.info[info_name]["label"].set_text(f"{info_name}: {info_value}")

    def debug_render(self, color):
        for info in self.info:
            self.info[info]["label"].render(color)
