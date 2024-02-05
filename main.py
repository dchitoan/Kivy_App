import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random
from word_generator import Word_List


class AppLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.word_list = Word_List()
        self.level.text = str(self.word_list.level_max)
        self.words = self.word_list.get_list(level=int(self.level.text))
        self.generate_word()

    def generate_word(self):
        word = random.choice(self.words)
        self.word_left.text = word[0]
        self.word_right.text = word[1]
        self.word_full.text = word[0] + word[1]

    def increase_nguyenam(self):
        if int(self.level.text) >= self.word_list.level_max:
            return
        self.level.text = str(int(self.level.text) + 1)
        self.words = self.word_list.get_list(level=int(self.level.text))
        self.generate_word()

    def decrease_nguyenam(self):
        if int(self.level.text) <= 1:
            return
        self.level.text = str(int(self.level.text) - 1)
        self.words = self.word_list.get_list(level=int(self.level.text))
        self.generate_word()


class ChuViet(App):
    def build(self):
        return AppLayout()


device = ChuViet()
device.run()
