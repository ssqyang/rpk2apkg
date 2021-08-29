import os
import re
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def is_capital_letter(char):
    return len(char) == 1 and char.isupper()


def convert_to_apkg_format(f):
    if not f:
        return ""
    f = f.replace("[audio:aws_", "[sound:")
    f = re.sub("\[image:(.*?)\]", r"<img src=\1>", f)
    f = re.sub("__(.*?)__", r"{{c1::\1}}", f)
    return f.strip()
