import sys
from tkinter import messagebox


class Messagebox:
    def __init__(self, title):
        self.title = title
        self.info = ""
        # redirect stdout to Messagebox
        self.stdout_bak = sys.stdout
        sys.stdout = self

    def write(self, info):
        self.info += info

    def send_message(self):
        if self.info:
            messagebox.showinfo(self.title, self.info)
        self.info = ""

    def clear(self):
        self.info = ""

    def flush(self):
        pass
