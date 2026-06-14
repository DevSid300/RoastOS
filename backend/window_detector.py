import pygetwindow as gw

def get_active_window():

    window = gw.getActiveWindow()

    if window:
        return window.title

    return "Unknown Window"


def get_all_windows():

    windows = gw.getAllTitles()

    # Remove empty titles
    windows = [w for w in windows if w.strip()]

    return windows