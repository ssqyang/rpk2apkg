# coding=utf-8
import os
import sys
import threading
import time
import traceback
from tkinter import Tk, messagebox, Label, Entry, StringVar, Button, filedialog

from message_stdout import Messagebox
from rpk_converter import RpkConverter
from util import resource_path


class App:
    def __init__(self, title):
        self.title = title
        self.root = Tk()
        self.root.title(title)
        self.rpk_file_path = StringVar()
        self.out_dir = StringVar()
        # layout
        Label(self.root, text="Select the rpk file:").grid(row=0, column=0)
        Entry(self.root, textvariable=self.rpk_file_path).grid(row=0, column=1)
        Button(self.root, text="select", command=self.select_rpk_file_path).grid(row=0, column=2)
        Label(self.root, text="Select the output directory:").grid(row=1, column=0)
        Entry(self.root, textvariable=self.out_dir).grid(row=1, column=1)
        Button(self.root, text="select", command=self.select_out_dir).grid(row=1, column=2)
        self.run_button = Button(self.root, text="run", width=15, command=self.touch_button)
        self.run_button.grid(row=2, column=0, columnspan=3)
        self.root.grid_rowconfigure(0, minsize=30)
        self.root.grid_rowconfigure(1, minsize=30)
        self.root.grid_rowconfigure(2, minsize=40)
        # window resize
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        self.root.geometry('+%d+%d' % ((screenwidth - 400) / 2, (screenheight - 100) / 2))
        self.root.resizable(width=False, height=False)
        # mainloop
        messagebox.showinfo(title, "This tool is used to convert rpk file to Anki apkg.")
        self.root.mainloop()

    def select_rpk_file_path(self):
        self.rpk_file_path.set(filedialog.askopenfilename())

    def select_out_dir(self):
        self.out_dir.set(filedialog.askdirectory())

    def touch_button(self):
        self.run_button.config(state="disabled")
        thread_convert = threading.Thread(target=self.run_convert)
        thread_convert.start()
        thread_count = threading.Thread(target=self.time_count)
        thread_count.start()

    def run_convert(self):
        rpk_file_path = self.rpk_file_path.get().replace("\\", "/")
        out_dir = self.out_dir.get().replace("\\", "/")
        sqlite_path = resource_path("static/template.sqlite3")
        if not out_dir:
            out_dir = os.getcwd().replace("\\", "/")

        message_stdout.clear()
        converter = RpkConverter(rpk_file_path, out_dir, sqlite_path)
        try:
            converter.read_rpk()
            converter.load_rpk_json()
            converter.write_to_sqlite()
            converter.convert_media_files()
            converter.pack_apkg()
        except Exception as e:
            messagebox.showerror(title, "**ERROR**\n" + str(
                e) + "\n\n To check the complete traceback error log, please open the console.")
            sys.stderr.write(traceback.format_exc())
        finally:
            converter.clear_tmp_files()
            message_stdout.send_message()
            self.run_button.config(text="run", state="normal")

    def time_count(self):
        count = 0
        while self.run_button['state'] == "disabled" and count < 1000:
            self.run_button['text'] = f"Converting...{count}s"
            count += 1
            time.sleep(1)


title = "RpkConverter"
message_stdout = Messagebox(title)
app = App(title=title)
