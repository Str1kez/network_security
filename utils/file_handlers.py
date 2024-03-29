from pathlib import Path
from tkinter import filedialog as fd
from typing import IO


def open_file() -> IO | None:
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))
    file = fd.askopenfile(
        title="Open file",
        initialdir=Path(__file__).parent.parent.resolve(),
        filetypes=filetypes,
    )
    return file
