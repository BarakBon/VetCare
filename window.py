from tkinter import ttk

def set_dpi():
    try:
        from ctypes import windll
        windll.shcore.Set.setPrecessDpiAwarness(1)
    except:
        pass


def window_spawn(window):
    #  position the screen at the middle of the screen
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(window.winfo_screenheight() / 2.5 - windowHeight / 2)

    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))

def set_style(window):
    style = ttk.Style(window)
    style.theme_use("clam")