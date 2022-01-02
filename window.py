from tkinter import ttk
import ctypes
import tkinter.font as font

def set_window(window):
    # set window dpi (set windows to high resolution)
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    font.nametofont("TkDefaultFont").configure(size=12)
    font.nametofont("TkTextFont").configure(size=12)

    #  position the screen at the middle of the screen
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(window.winfo_screenheight() / 4 - windowHeight / 2)

    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))

    #  set window style
    style = ttk.Style(window)
    # style.theme_use("clam")
    # print(style.layout("TLabel"))
    # print(style.element_options("Label.border"))
    # style.configure("Label", backround="white")